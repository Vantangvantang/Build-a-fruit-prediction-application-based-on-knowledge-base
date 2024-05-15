# importing durable rules engine library
from durable.lang import *

def assert_fact_with_error_check(ruleset_name, fact):
    # Thực thi quy tắc và nhận kết quả trả về
    result = assert_fact(ruleset_name, fact)
    
    # Kiểm tra xem kết quả có được trả về không
    if result is None:
        print("Lỗi: Không có kết quả trả về từ quy tắc '{0}' với dữ liệu '{1}'".format(ruleset_name, fact))



# 'fruit' facts to suggest the fruit  by Users interest. 
with ruleset('fruit'):
    # When the user enters the shape: long or round , Color : green or yellow
    #R3: (long v round)  ^  (green v yellow) => banana
    @when_all( (m.shape == 'Long') & (m.color == 'Green' ))
    def fruit_sugg_ai(fr):
      # triggering characteristic fact to find fruit names
        fr.assert_fact({'fruit_type':'Banana'})
    
    @when_all( (m.shape == 'Long')  & (m.color == 'Yellow'))
    def fruit_sugg_ai(fr):
      # triggering characteristic fact to find fruit names
        fr.assert_fact({'fruit_type':'Banana'})
    
    @when_all( (m.shape == 'Round')  & (m.color == 'Green'))
    def fruit_sugg_ai(fr):
      # triggering characteristic fact to find fruit names
        fr.assert_fact({'fruit_type':'Banana'})
    
    @when_all( (m.shape == 'Round')  & (m.color == 'Yellow'))
    def fruit_sugg_ai(fr):
      # triggering characteristic fact to find fruit names
        fr.assert_fact({'fruit_type':'Banana'})
    
    #R4:  vine ^  green => watermelon
    @when_all( (m.fruitclass == 'Vines') & (m.color == 'Green'))
    def fruit_sugg_ai(fr):
        fr.assert_fact({'fruit_type':'Watermelon'})
    
    @when_all( (m.shape == 'Round') & (m.diameter > '4') & (m.color == 'Green'))
    def fruit_sugg_ai(fr):
        fr.assert_fact({'fruit_type':'Watermelon'})
    
    @when_all( (m.shape == 'Oblong') & (m.diameter > '4') & (m.color == 'Green'))
    def fruit_sugg_ai(fr):
        fr.assert_fact({'fruit_type':'Watermelon'})
      
    #R5:  vine ^  smooth ^ yellow=> honeydew
    @when_all( (m.fruitclass == 'Vines')  & (m.surface == 'Smooth') & (m.color == 'Yellow'))
    def fruit_sugg_ai(fr):
        fr.assert_fact({'fruit_type':'Honeydew'})
    
    @when_all( (m.shape == 'Round') & (m.diameter > '4') & (m.surface == 'Smooth') & (m.color == 'Yellow'))
    def fruit_sugg_ai(fr):
        fr.assert_fact({'fruit_type':'Honeydew'})
    
    @when_all( (m.shape == 'Oblong') & (m.diameter > '4')  & (m.surface == 'Smooth') & (m.color == 'Yellow'))
    def fruit_sugg_ai(fr):
        fr.assert_fact({'fruit_type':'Honeydew'})
    
    #R6:  vine ^ rough ^ tan => cantaloupe
    @when_all((m.fruitclass == 'Vines') & (m.surface == 'Rough') & (m.color == 'Tan'))
    def fruit_sugg_ai(fr):
        fr.assert_fact({'fruit_type':'Cantaloupe'})
    
    @when_all((m.shape == 'Round') & (m.diameter > '4') & (m.surface == 'Rough') & (m.color == 'Tan'))
    def fruit_sugg_ai(fr):
        fr.assert_fact({'fruit_type':'Cantaloupe'})
    
    @when_all((m.shape == 'Oblong') & (m.diameter > '4') & (m.surface == 'Rough') & (m.color == 'Tan'))
    def fruit_sugg_ai(fr):
        fr.assert_fact({'fruit_type':'Cantaloupe'})
    
    
    #R7: tree ^ multiple ^ (green v yellow v red )  => apple
    @when_all((m.fruitclass == 'Tree') & (m.seedclass == 'Multiple') & (m.color == 'Green'))
    def fruit_sugg_ai(fr):
        fr.assert_fact({'fruit_type':'Apple'})
    
    @when_all((m.fruitclass == 'Tree') & (m.seedcount > '1') & (m.color == 'Green'))
    def fruit_sugg_ai(fr):
        fr.assert_fact({'fruit_type':'Apple'})
    
    @when_all((m.shape == 'Round') & (m.diameter <= '4') & (m.seedclass == 'Multiple') & (m.color == 'Green'))
    def fruit_sugg_ai(fr):
        fr.assert_fact({'fruit_type':'Apple'})
    
    @when_all((m.shape == 'Round') & (m.diameter <= '4') & (m.seedcount > '1')& (m.color == 'Green'))
    def fruit_sugg_ai(fr):
        fr.assert_fact({'fruit_type':'Apple'})
    
    @when_all((m.fruitclass == 'Tree') & (m.seedclass == 'Multiple') & (m.color == 'Yellow'))
    def fruit_sugg_ai(fr):
        fr.assert_fact({'fruit_type':'Apple'})
    
    @when_all((m.fruitclass == 'Tree') & (m.seedcount > '1') & (m.color == 'Yellow'))
    def fruit_sugg_ai(fr):
        fr.assert_fact({'fruit_type':'Apple'})
    
    
    @when_all((m.shape == 'Round') & (m.diameter <= '4') & (m.seedclass == 'Multiple') & (m.color == 'Yellow'))
    def fruit_sugg_ai(fr):
        fr.assert_fact({'fruit_type':'Apple'})
    
    @when_all((m.shape == 'Round') & (m.diameter <= '4') & (m.seedcount > '1') & (m.color == 'Yellow'))
    def fruit_sugg_ai(fr):
        fr.assert_fact({'fruit_type':'Apple'})
    
    @when_all((m.fruitclass == 'Tree') & (m.seedclass == 'Multiple') & (m.color == 'Red'))
    def fruit_sugg_ai(fr):
        fr.assert_fact({'fruit_type':'Apple'})
    
    @when_all((m.fruitclass == 'Tree') & (m.seedcount > '1') & (m.color == 'Red'))
    def fruit_sugg_ai(fr):
        fr.assert_fact({'fruit_type':'Apple'})
    
    @when_all((m.shape == 'Round') & (m.diameter <= '4') & (m.seedclass == 'Multiple') & (m.color == 'Red'))
    def fruit_sugg_ai(fr):
        fr.assert_fact({'fruit_type':'Apple'})
    
    @when_all((m.shape == 'Round') & (m.diameter <= '4') & (m.seedcount > '1') & (m.color == 'Red'))
    def fruit_sugg_ai(fr):
        fr.assert_fact({'fruit_type':'Apple'})
      
    # R8: tree ^ orange ^  stonefruit => apricot
    @when_all((m.fruitclass == 'Tree') & (m.seedclass == 'Stonefruit') & (m.color == 'Orange'))
    def fruit_sugg_ai(fr):
        fr.assert_fact({'fruit_type':'Apricot'})
    
    @when_all((m.fruitclass == 'Tree') & (m.seedcount == '1') & (m.color == 'Orange'))
    def fruit_sugg_ai(fr):
        fr.assert_fact({'fruit_type':'Apricot'})
    
    
    @when_all((m.shape == 'Round') & (m.diameter <= '4') & (m.seedclass == 'Stonefruit') & (m.color == 'Orange'))
    def fruit_sugg_ai(fr):
        fr.assert_fact({'fruit_type':'Apricot'})
    
    @when_all((m.shape == 'Round') & (m.diameter <= '4') & (m.seedcount == '1') & (m.color == 'Orange'))
    def fruit_sugg_ai(fr):
        fr.assert_fact({'fruit_type':'Apricot'})
    
    #R9: tree ^ red ^  stonefruit => cherry
    @when_all((m.fruitclass == 'Tree') & (m.seedclass == 'Stonefruit') & (m.color == 'Red'))
    def fruit_sugg_ai(fr):
        fr.assert_fact({'fruit_type':'Cherry'}) 
    
    @when_all((m.fruitclass == 'Tree') & (m.seedcount == '1') & (m.color == 'Red'))
    def fruit_sugg_ai(fr):
        fr.assert_fact({'fruit_type':'Cherry'}) 
    
    @when_all((m.shape == 'Round') & (m.diameter <= '4') & (m.seedclass == 'Stonefruit') & (m.color == 'Red'))
    def fruit_sugg_ai(fr):
        fr.assert_fact({'fruit_type':'Cherry'}) 
    
    @when_all((m.shape == 'Round') & (m.diameter <= '4') & (m.seedcount == '1') & (m.color == 'Red'))
    def fruit_sugg_ai(fr):
        fr.assert_fact({'fruit_type':'Cherry'}) 
    
    #R10: tree ^ orange ^ multiple => orange
    @when_all((m.fruitclass == 'Tree') & (m.seedclass == 'Multiple') & (m.color == 'Orange'))
    def fruit_sugg_ai(fr):
        fr.assert_fact({'fruit_type':'Orange'})
    
    @when_all((m.fruitclass == 'Tree') & (m.seedcount == '1') & (m.color == 'Orange'))
    def fruit_sugg_ai(fr):
        fr.assert_fact({'fruit_type':'Orange'})
    
    @when_all((m.shape == 'Round') & (m.diameter <= '4') & (m.seedclass == 'Multiple') & (m.color == 'Orange'))
    def fruit_sugg_ai(fr):
        fr.assert_fact({'fruit_type':'Orange'})
    
    @when_all((m.shape == 'Round') & (m.diameter <= '4') & (m.seedcount == '1') & (m.color == 'Orange'))
    def fruit_sugg_ai(fr):
        fr.assert_fact({'fruit_type':'Orange'})
    
    #R11: tree ^ orange ^  stonefruit => peach
    @when_all((m.fruitclass == 'Tree') & (m.seedclass == 'Stonefruit') & (m.color == 'Orange'))
    def fruit_sugg_ai(fr):
        fr.assert_fact({'fruit_type':'Peach'})
    
    @when_all((m.fruitclass == 'Tree') & (m.seedcount == '1') & (m.color == 'Orange'))
    def fruit_sugg_ai(fr):
        fr.assert_fact({'fruit_type':'Peach'})
    
    @when_all((m.shape == 'Round') & (m.diameter <= '4') & (m.seedclass == 'Stonefruit') & (m.color == 'Orange'))
    def fruit_sugg_ai(fr):
        fr.assert_fact({'fruit_type':'Peach'})
    
    @when_all((m.shape == 'Round') & (m.diameter <= '4') & (m.seedcount == '1') & (m.color == 'Orange'))
    def fruit_sugg_ai(fr):
        fr.assert_fact({'fruit_type':'Peach'})
    
    #R12: tree ^ purple ^ stonefruit  => plume
    @when_all((m.fruitclass == 'Tree') & (m.seedclass == 'Stonefruit') & (m.color == 'Purple'))
    def fruit_sugg_ai(fr):
        fr.assert_fact({'fruit_type':'Plume'})
        
    @when_all((m.fruitclass == 'Tree') & (m.seedcount == '1') & (m.color == 'Purple'))
    def fruit_sugg_ai(fr):
        fr.assert_fact({'fruit_type':'Plume'})

    @when_all((m.shape == 'Round') & (m.diameter <= '4') & (m.seedclass == 'Stonefruit') & (m.color == 'Purple') )
    def fruit_sugg_ai(fr):
        fr.assert_fact({'fruit_type':'Plume'})
    
    @when_all((m.shape == 'Round') & (m.diameter <= '4') & (m.seedcount == '1') & (m.color == 'Purple') )
    def fruit_sugg_ai(fr):
        fr.assert_fact({'fruit_type':'Plume'})
    
    #Output all Suggestions
    @when_all(+m.fruit_type)
    def output(fr):
        print('fruit_type: {0}'.format(fr.m.fruit_type))

#start program
print('Welcome to the fruit prediction game')
print('What does the fruit look like? Please enter an option ')
print(' 1) Long   2) Round   3) Oblong')
shapes = input()
print('Diameter ?')
print(' 1) Diameter >4    2) Diameter <4')
dia_meter = str(input())
print('Surface ?')
print(' 1) Smooth   2) rough ')
sur_face = input()
print('Color ?')
print(' 1) Green    2) Yellow  3) Tan   4) Orange  5) Red   6) Purple')
colors = input()
print('Seedclass ?')
print(' 1) Multiple    2) Stonefruit')
seed_class = input()
print('Seedcount ?')
print(' 1) >1    2) =1')
seed_count = str(input())
print('Fruitclass ?')
print(' 1) Vines    2) Tree ')
fruit_class = input()

print('*******************************************************************************************************')
#triggering fact course
assert_fact_with_error_check('fruit', { 'shape': shapes,'diameter': dia_meter, 'surface': sur_face, 'color': colors,'seedclass': seed_class,'seedcount': seed_count,'fruitclass': fruit_class})

print('*******************************************************************************************************')
    

    