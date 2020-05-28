"""
day 7 lec
"""
i = 5

#while i >= 0:
#    print(i)
#    i = i -1        #make sure at some pt condition will be false
    
#while i >= 0:
#    i = i -1
#    if i == 3:
#        break      #stops loop if meets condition in line above^^
#    print(i)
    
#while i >= 0:
#    i = i -1
#    if i == 3:
#        continue    #skips condition in 'if' statement^^
#    print(i)
    
#while i >= 0:
#    i = i -1
#    if i == 3:
#        pass        #does nothing, prevents syntax error in 'if' statement
#    print(i)

#try:
#    print(1/0)
#except ZeroDivisionError:
#    print('error')

while i >= 0:
    try:
        print(1/(i-3))
    except:
        pass
    i = i - 1

