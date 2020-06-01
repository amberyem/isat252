"""
lab 8
"""
#3.1
#def calcwords(input_str):
#    return len(input_str.split())
    
#3.2
#demo_str = 'hello world!'
#print(calcwords(demo_str))

#3.3
def calnum(input_list):
    min_item = input_list[0]
    
    for eachnum in input_list:
        if type(eachnum) is not str:
            if min_item >= eachnum:
                min_item = eachnum
            
    return min_item
            
#3.4
num_list = [1,2,3,4,5,6]
print(calnum(num_list))

#3.5
mix_list = [1,2,3,4,'a',5,6]
print(calnum(mix_list))
