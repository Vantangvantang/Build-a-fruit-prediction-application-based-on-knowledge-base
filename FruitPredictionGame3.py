import tkinter as tk
from tkinter import ttk
from durable.lang import *
import random
import BackwardChaining as BC

class FruitPredictor:
    def __init__(self, root):
        self.root = root
        self.root.title("Fruit Predictor")

        self.predicted_fruit = None
        self.random_fruit = None

        # Create and place widgets for Forward Chaining
        tk.Label(root, text="Forward Chaining").grid(row=0, column=0, columnspan=2)

        tk.Label(root, text="Shape").grid(row=1, column=0)
        self.shape_var = tk.StringVar()
        self.shape_menu = ttk.Combobox(root, textvariable=self.shape_var, state="readonly")
        self.shape_menu['values'] = ("Long", "Round", "Oblong")
        self.shape_menu.grid(row=1, column=1)

        tk.Label(root, text="Diameter (inch)").grid(row=2, column=0)
        self.diameter_var = tk.StringVar()
        self.diameter_entry = ttk.Spinbox(root, from_=0, to=10, textvariable=self.diameter_var)
        self.diameter_entry.grid(row=2, column=1)

        tk.Label(root, text="Surface").grid(row=3, column=0)
        self.surface_var = tk.StringVar()
        self.surface_menu = ttk.Combobox(root, textvariable=self.surface_var, state="readonly")
        self.surface_menu['values'] = ("Smooth", "Rough")
        self.surface_menu.grid(row=3, column=1)

        tk.Label(root, text="Color").grid(row=4, column=0)
        self.color_var = tk.StringVar()
        self.color_menu = ttk.Combobox(root, textvariable=self.color_var, state="readonly")
        self.color_menu['values'] = ("Green", "Yellow", "Tan", "Orange", "Red", "Purple")
        self.color_menu.grid(row=4, column=1)

        tk.Label(root, text="Seed Class").grid(row=5, column=0)
        self.seed_class_var = tk.StringVar()
        self.seed_class_menu = ttk.Combobox(root, textvariable=self.seed_class_var, state="readonly")
        self.seed_class_menu['values'] = ("Multiple", "Stonefruit")
        self.seed_class_menu.grid(row=5, column=1)

        tk.Label(root, text="Fruit Class").grid(row=6, column=0)
        self.fruit_class_var = tk.StringVar()
        self.fruit_class_menu = ttk.Combobox(root, textvariable=self.fruit_class_var, state="readonly")
        self.fruit_class_menu['values'] = ("Vines", "Tree")
        self.fruit_class_menu.grid(row=6, column=1)

        tk.Label(root, text="Seed Count").grid(row=7, column=0)
        self.seed_count_var = tk.StringVar()
        self.seed_count_menu = ttk.Combobox(root, textvariable=self.seed_count_var, state="readonly")
        self.seed_count_menu['values'] = (">1", "=1")
        self.seed_count_menu.grid(row=7, column=1)

        self.predict_button = tk.Button(root, text="Predict Fruit", command=self.predict_fruit)
        self.predict_button.grid(row=8, column=0)

        self.reset_button = tk.Button(root, text="Reset", command=self.reset_fields)
        self.reset_button.grid(row=8, column=1)

        self.selected_fruit_label = tk.Label(root, text="Fruit: ...")
        self.selected_fruit_label.grid(row=9, column=0, columnspan=2)

        # Fruit Mix label
        self.random_fruit_label = tk.Label(root, text="Fruit Mix: ...")
        self.random_fruit_label.grid(row=10, column=0, columnspan=2)

        # Create and place widgets for Backward Chaining
        tk.Label(root, text="Backward Chaining").grid(row=0, column=2, columnspan=2)

        tk.Label(root, text="Fruit").grid(row=1, column=2)
        self.backward_fruit_var = tk.StringVar()
        self.backward_fruit_menu = ttk.Combobox(root, textvariable=self.backward_fruit_var, state="readonly")
        self.backward_fruit_menu['values'] = ("Banana", "Watermelon", "Honeydew", "Cantaloupe", "Apple", "Apricot", "Cherry", "Orange", "Peach", "Plume", "b")
        self.backward_fruit_menu.grid(row=1, column=3)

        self.backward_steps_text = tk.Text(root, width=40, height=10, state="disabled")
        self.backward_steps_text.grid(row=2, column=2, rowspan=6, columnspan=2)

        self.backward_fruit_menu.bind("<<ComboboxSelected>>", self.display_backward_steps)

        self.result_label = tk.Label(root, text="", font=("Arial", 24))
        self.result_label.grid(row=11, column=0, columnspan=4)

        self.generate_random_fruit()

    def predict_fruit(self):
        fact = {
            'shape': self.shape_var.get().strip().lower(),
            'diameter': str(self.diameter_var.get()),  # Convert to string for the rule engine
            'surface': self.surface_var.get().strip().lower(),
            'color': self.color_var.get().strip().lower(),
            'seedclass': self.seed_class_var.get().strip().lower(),
            'seedcount': self.seed_count_var.get().strip().lower(),
            'fruitclass': self.fruit_class_var.get().strip().lower()
        }

        # Kiểm tra các giá trị đầu vào
        if not all(fact.values()):
            self.selected_fruit_label.config(text="Please fill in all fields.")
            return

        self.predicted_fruit = None
        assert_fact_with_error_check('fruit', fact)
        if self.predicted_fruit:
            self.selected_fruit_label.config(text=f"Fruit: {self.predicted_fruit}")
            if self.predicted_fruit == self.random_fruit:
                self.show_result(True)
            else:
                self.show_result(False)
        else:
            self.selected_fruit_label.config(text="Fruit: Please use another set of rules!!!!")

    def reset_fields(self):
        self.shape_var.set('')
        self.diameter_var.set(0)
        self.surface_var.set('')
        self.color_var.set('')
        self.seed_class_var.set('')
        self.fruit_class_var.set('')
        self.seed_count_var.set('')
        self.selected_fruit_label.config(text="Fruit: ...")
        self.random_fruit_label.config(text="Fruit Mix: ...")
        self.backward_steps_text.config(state="normal")
        self.backward_steps_text.delete("1.0", tk.END)
        self.backward_steps_text.config(state="disabled")
        self.predicted_fruit = None
        self.random_fruit = None
        self.result_label.config(text="")
        # Thêm phần này để đảm bảo rằng rule engine cũng được reset
        self.clear_rules('fruit')
        self.generate_random_fruit()

    def display_backward_steps(self, event):
        selected_fruit = self.backward_fruit_var.get().strip().lower()
        goal = selected_fruit

        goal_list, num_back, VET = BC.excute_backward_chaining(goal, BC.rules)
        # Xóa nội dung hiện có trong Text widget
        self.backward_steps_text.config(state="normal")
        self.backward_steps_text.delete("1.0", tk.END)

        # Thêm giá trị của num_back và VET
        self.backward_steps_text.insert(tk.END, f"\nnum_back: {num_back}\n")
        self.backward_steps_text.insert(tk.END, f"VET: {VET}\n")

        # Thực hiện backward chaining
        if not goal_list:
            self.backward_steps_text.insert(tk.END, "\nResult: True")
        else:
            self.backward_steps_text.insert(tk.END, "\nResult: False")

        # Khóa Text widget lại
        self.backward_steps_text.config(state="disabled")

    def clear_rules(self, ruleset_name):
        # Hàm này để reset lại các rule đã được assert
        try:
            delete_state(ruleset_name)
        except Exception as e:
            print(f"Error clearing rules: {e}")

    def generate_random_fruit(self):
        fruits = ["Banana", "Watermelon", "Honeydew", "Cantaloupe", "Apple", "Apricot", "Cherry", "Orange", "Peach", "Plume"]
        self.random_fruit = random.choice(fruits)
        self.random_fruit_label.config(text=f"Fruit Mix: {self.random_fruit}")

    def show_result(self, is_correct):
        if is_correct:
            self.result_label.config(text="TRUE", fg="green")
        else:
            self.result_label.config(text="FALSE", fg="red")

def assert_fact_with_error_check(ruleset_name, fact):
    try:
        assert_fact(ruleset_name, fact)
    except Exception as e:
        print(f"Error asserting fact: {e}")

with ruleset('fruit'):
    @when_all((m.shape == 'long') & (m.color == 'yellow'))
    def fruit_pre_ba(fr):
        fr.assert_fact({'fruit_type': 'Banana'})
    @when_all((m.shape == 'long') & (m.color == 'green'))
    def fruit_pre_ba(fr):
        fr.assert_fact({'fruit_type': 'Banana'})
    @when_all((m.shape == 'round') & (m.color == 'yellow'))
    def fruit_pre_ba(fr):
        fr.assert_fact({'fruit_type': 'Banana'})
    @when_all((m.shape == 'round') & (m.color == 'green'))
    def fruit_pre_ba(fr):
        fr.assert_fact({'fruit_type': 'Banana'})
    @when_all((m.fruitclass == 'vines') & (m.color == 'green'))
    def fruit_pre_wa(fr):
        fr.assert_fact({'fruit_type': 'Watermelon'})
    @when_all((m.shape == 'round') & (m.diameter > '4') & (m.color == 'green'))
    def fruit_pre_wa(fr):
        fr.assert_fact({'fruit_type': 'Watermelon'})
    @when_all((m.shape == 'oblong') & (m.diameter > '4') & (m.color == 'green'))
    def fruit_pre_wa(fr):
        fr.assert_fact({'fruit_type': 'Watermelon'})
    @when_all((m.fruitclass == 'vines') & (m.surface == 'smooth') & (m.color == 'yellow'))
    def fruit_pre_ho(fr):
        fr.assert_fact({'fruit_type': 'Honeydew'})
    @when_all((m.shape == 'round') & (m.diameter > '4') & (m.surface == 'smooth') & (m.color == 'yellow'))
    def fruit_pre_ho(fr):
        fr.assert_fact({'fruit_type': 'Honeydew'})
    @when_all((m.fruitclass == 'vines') & (m.surface == 'rough') & (m.color == 'yellow'))
    def fruit_pre_ca(fr):
        fr.assert_fact({'fruit_type': 'Cantaloupe'})
    @when_all((m.shape == 'round') & (m.diameter > '4') & (m.surface == 'rough') & (m.color == 'yellow'))
    def fruit_pre_ca(fr):
        fr.assert_fact({'fruit_type': 'Cantaloupe'})
    @when_all((m.fruitclass == 'tree') & (m.color == 'green') & (m.seedclass == 'multiple'))
    def fruit_pre_ap(fr):
        fr.assert_fact({'fruit_type': 'Apple'})
    @when_all((m.fruitclass == 'tree') & (m.color == 'tan') & (m.seedclass == 'multiple'))
    def fruit_pre_ap(fr):
        fr.assert_fact({'fruit_type': 'Apricot'})
    @when_all((m.fruitclass == 'tree') & (m.color == 'red') & (m.seedclass == 'multiple'))
    def fruit_pre_ch(fr):
        fr.assert_fact({'fruit_type': 'Cherry'})
    @when_all((m.fruitclass == 'tree') & (m.color == 'tan') & (m.seedcount == '=1'))
    def fruit_pre_pe(fr):
        fr.assert_fact({'fruit_type': 'Peach'})
    @when_all((m.fruitclass == 'tree') & (m.color == 'orange') & (m.seedcount == '=1'))
    def fruit_pre_pe(fr):
        fr.assert_fact({'fruit_type': 'Peach'})
    @when_all((m.fruitclass == 'tree') & (m.color == 'purple') & (m.seedcount == '=1'))
    def fruit_pre_pl(fr):
        fr.assert_fact({'fruit_type': 'Plume'})

    @when_all((m.fruit_type == 'Banana'))
    def classify_fruit(c):
        c.s.label = 'Banana'
        fruit_predictor.predicted_fruit = 'Banana'

    @when_all((m.fruit_type == 'Watermelon'))
    def classify_fruit(c):
        c.s.label = 'Watermelon'
        fruit_predictor.predicted_fruit = 'Watermelon'

    @when_all((m.fruit_type == 'Honeydew'))
    def classify_fruit(c):
        c.s.label = 'Honeydew'
        fruit_predictor.predicted_fruit = 'Honeydew'

    @when_all((m.fruit_type == 'Cantaloupe'))
    def classify_fruit(c):
        c.s.label = 'Cantaloupe'
        fruit_predictor.predicted_fruit = 'Cantaloupe'

    @when_all((m.fruit_type == 'Apple'))
    def classify_fruit(c):
        c.s.label = 'Apple'
        fruit_predictor.predicted_fruit = 'Apple'

    @when_all((m.fruit_type == 'Apricot'))
    def classify_fruit(c):
        c.s.label = 'Apricot'
        fruit_predictor.predicted_fruit = 'Apricot'

    @when_all((m.fruit_type == 'Cherry'))
    def classify_fruit(c):
        c.s.label = 'Cherry'
        fruit_predictor.predicted_fruit = 'Cherry'

    @when_all((m.fruit_type == 'Peach'))
    def classify_fruit(c):
        c.s.label = 'Peach'
        fruit_predictor.predicted_fruit = 'Peach'

    @when_all((m.fruit_type == 'Plume'))
    def classify_fruit(c):
        c.s.label = 'Plume'
        fruit_predictor.predicted_fruit = 'Plume'

if __name__ == "__main__":
    root = tk.Tk()
    fruit_predictor = FruitPredictor(root)
    root.mainloop()
