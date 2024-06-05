#method overriding in POOP

# Method overriding is a feature of OOP that allows a subclass to provide a specific implementation of a method that is already provided 
# by its superclass.

#Example of method overring in POOP
import math as m
#parent class:shape
class shape:
    
    #initialize using constructor
    def __init__(self,a,b) -> None:
        self.a = a
        self.b = b
    
    def area(self):
        return (self.a * self.b)


#child class: sphere

class sphere(shape):
        
        #initialize using constructor
        def __init__(self,a) -> None:
            self.a = a
        
        #overriding method
        def area(self):
            return 4*m.pi*(self.a**2)

rectangle = shape(3,4)
print("Area of rectangle: ",rectangle.area())

#creating object of child class sphere

sp = sphere(7)
print("Area of sphere: ",sp.area())