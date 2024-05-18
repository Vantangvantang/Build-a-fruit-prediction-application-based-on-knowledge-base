def read_rules(filename):
    with open(filename, 'r') as file:
        return [line.replace('&&', '^').strip() for line in file]

def show_rules(rules):
    for i, rule in enumerate(rules, start=1):
        print(f"Rule {i}: {rule}")

def split_rule(rule):
    parts = rule.split(" => ")
    condition = parts[0]
    result = parts[1]
    condition = condition.replace('||', '').replace('^', '').replace('(', '').replace(')', '')
    splited_condition_list = condition.split()
    return condition, result, splited_condition_list

def excute_backward_chaining(goal, rules):
    num_back = 0
    goal_list = [goal]
    VET = []
    known_facts = ["long", "round", "oblong", "diameterabove4", "diameterbelow4", "smooth", "rough", "green", "yellow", "tan", "orange", "red", "purple", "countseedabove1", "countseedbelow1"]
    while goal_list:
        is_goal_list_changed = False            
        print(f'============== current goal_list: {goal_list} ==============')
        for goal in goal_list:
            VET.append(goal)
            for rule in rules:
                print(f'***** {rule} *****')
                condition, result, splited_condition_list = split_rule(rule)
                if goal == result:
                    print(f'{goal} = {result}')
                    print('- splited_condition_list: ',splited_condition_list)
                    newsplited_condition_list = []
                    for item in splited_condition_list:
                        print('  + item: ', item)
                        if item in known_facts:
                            print(f'  + remove {item}')
                        else:
                            print(f'  + {item} not in known_facts: ')
                            newsplited_condition_list.append(item)
                    print("---------------------")
                    goal_list.remove(goal)
                    goal_list.extend(newsplited_condition_list)
                    is_goal_list_changed = True
                    continue
                else:
                    print(f'{goal} != {result}')
            if is_goal_list_changed:
                break
        if not is_goal_list_changed:
            break
        else:
            num_back += 1
        print(f"=> goal_list= {goal_list}\n   num_back= {num_back}\n   VET= {VET}")
    return goal_list, num_back, VET       

rules = read_rules("rules.txt")
show_rules(rules)