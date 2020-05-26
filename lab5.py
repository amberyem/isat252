"""
5th python lab
"""

#3.1
#alien_color = 'green'

#if alien_color == 'green':
#    print("You just earned 5 points!")

    
#3.2
alien_color = 'blue'

if alien_color == 'green':
    print("You just earned 5 points!")
else:
    print("You just earned 10 points!")

    
#3.3
favorite_fruits = ['apple', 'strawberry', 'blackberry']

if 'apple' in favorite_fruits:
    print('You really like apples!')

if 'grape' in favorite_fruits:
        print('You really like grapes!')
        
if 'strawberry' in favorite_fruits:
    print('You really like strawberries!')

if 'orange' in favorite_fruits:
    print('You really like oranges!') 
    
if 'blackberry' in favorite_fruits:
    print('You really like blackberries!')
    
    
#3.4
age =  70

if age < 10:
    print("You are a kid.")
elif age < 20:
    print("You are a teenager.")
else:
    print("You are an adult.")
    if age >65:
        print("You are an elder.")