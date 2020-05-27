"""
day 6 lecture
"""
demo_str = 'this is my string'


#for each_string in demo_str:
#    print(each_string)

#for each_word in demo_str.split():  #.split creates list
#    print(each_word.upper())
#    print(each_word.title())
    
#for each_word in demo_str.split():
#    if each_word == 'my':
#        print(each_word)
        
#for each_word in demo_str.split():
#    print(each_word)
#    for each_string in each_word:
#        print(each_string)


#for each_num in range(1,5):
#    print(each_num)
    
    
num_list = [213,321,123,312]
    
max_item = num_list[0]

for eachnum in num_list:
    if max_item <= eachnum:
        max_item = eachnum
print(max_item)    
    