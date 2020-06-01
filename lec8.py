"""
lecture 8
functions
"""
#def my_function(a,b):
#    result = a + b
    
#    print('a is' ,a)
#    print('b is' ,b)
#    return result
    


#print(my_function(1,2))     #positional argument: default, order affects what variables are defined as
#print(my_function(a=2,b=1))     #keyword argument: defining args so order doesn't matter


#ex1

#def calculate_abs(a):
#    if type(a) is str:
#        return ('wrong data type')
#    elif a >=0:
#        return a
#    else:
#        return -a
#        
#print(calculate_abs(0))
'''
#ex2

def calculate_sigma(m,n):
    result = 0
    for i in range(m,n+1): 
        result = result + i

    return result
    
print(calculate_sigma(3,5))

#ex2.1
def calculate_pi(m,n):
    result = 1
    for i in range(m,n+1): 
        result = result * i

    return result
    
print(calculate_pi(3,5))
'''
#ex3

def cal_f(m):
    if m == 0:
        return 1
    else:
        return m * cal_f(m-1)
        
print(cal_f(3))

#ex3.1
def cal_p(m,n):
    return cal_f(m)/cal_f(m-n)
    
print(cal_p(5,3))

    