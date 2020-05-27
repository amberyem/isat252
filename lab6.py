"""
lab 6
"""
#3.1
#for each_num in range(0,6):
#    if each_num != 3:
#        print(each_num)
    
    

#3.2
#factorial = 1

#for each_num in range(1,6):
#    factorial = factorial * each_num
    
#print(factorial)



#3.3
#i = 0

#for each_num in range(1,6):
#    i = i + each_num
    
#print(i)



#3.4
#k = 1

#for each_num in range(3,9):
#    k = k * each_num
    
#print(k)


#3.5
#n = 1
#for each_num in range(1,9):
#    n = n * each_num
    
#d = 1
#for num2 in range(1,4):
#    d = d * num2
    
#print(n / d)



#3.6
#my_str = 'this is my 6th string'
#execute = 0

#for each_str in my_str.split():
#    execute = execute + 1

#print(execute)



#3.7
my_tweet = {
    
        "favorite_count":1138,
        "lang": "en",
        "coordinates": (-75, 40),
        "entities": {"hashtags": [" Preds ", "Pens",
        " SingIntoSpring "]}

            }
            
num_hash = 0
dictionary = my_tweet['entities']['hashtags']

for each_ent in dictionary:
    num_hash = num_hash + 1
    
print(num_hash)

