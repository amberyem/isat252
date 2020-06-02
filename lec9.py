"""
lec9. class
"""
class car:                  #class name
    maker = 'toyota'        #shared attribute
    def __init__(self, input_model):  #unique attribute
        self.model = input_model
        
my_corolla = car('corolla')     #user defines own attribute of instance
print(my_corolla.maker)
print(my_corolla.model)
'''    def report_maker(self):     #method. always need .self 1st
        return(self.maker)  #what does function do?
        
        
my_car = car()          #create an instance/object from the class

print(my_car.maker)'''