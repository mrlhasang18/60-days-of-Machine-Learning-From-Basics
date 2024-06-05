#This is day 5 of learning machine learning from the beginning.
'''

Abstraction is the concept of hiding the complex implementation details 
and showing only the necessary features of the object.


Emcapsulation is the concept in OOP that binds the data and method together as a single unit. such as class.

'''

# Example of abstraction and encapsulation in Python
print('\n------------------ DAY 5 ----------------\n')

class car:
    #attributes
    name = None
    milage = None
    
    #initializing attributes using constructor
    def __init__(self,name,milage) -> None:
        self.name = name
        self.milage = milage
        
    def display(self) -> None:
        print(f"{self.name} gives {self.milage} milage.")
    
    def update_milage(self,milage):
        #update car milage
        self.milage = milage
        return self.milage
    
    def update_name(self,name):
        #update car name
        self.name = name
        return self.name

#creating object of car class

car1 = car("Lamborgini",200)
print(car1.name)
car1.display()
print(car1.update_milage("300"),car1.update_name("Ferari"))
car1.display()


# In the Car class, attributes (name and mileage) and methods (get_milage and get_name) are bound together as a single unit, 
# demonstrating encapsulation. Additionally, we've abstracted away the complex implementation, only showing the necessary details.