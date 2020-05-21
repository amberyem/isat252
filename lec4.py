"""
lecture day 4 notes. tuple and dictionary
"""
#my_tuple = 'a','b','c','d','e'

#print(my_tuple)

#print(my_tuple[0])
#print(my_tuple[0:4])

#my_2nd_tuple = ('a', 'b', 'c', 'd', 'e')
#with or without parenthesis is fine, commas matter

#print(my_2nd_tuple)


my_car = {
    'color':'red',
    'maker':'toyota',
    'year': 2015
}

#print(my_car['year'])
#print(my_car.get('year'))

my_car['model'] = 'corolla'
my_car['year'] = 2020

print('mile' in my_car)
print(len(my_car))