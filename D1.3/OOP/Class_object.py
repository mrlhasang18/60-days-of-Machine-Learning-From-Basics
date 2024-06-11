'''1>class: blueprint or template that defines characteristics and behaviour of object
   class consists of:
    attributes: data that object holds
    methods: functions that object can perform
   2>Objects: instance of class
   
   constructor: special method called when object of an class is created
   
   in python it's syntax is:
    def __init__(self):
    
    '''
    
class Car:
    
    #attributes
    model = None
    year = None
    color = None
    
    #constructor
    def __init__(self, model, year, color):
        self.model = model
        self.year = year
        self.color = color
    
    
    #behaviours or functions or methods
    def drive(self):
        print("Driving "+self.model+" Car")
    def stop(self):
        print("Stopping "+self.model+" Car")
        
#object calling
        
car_a = Car("bugati",2024,"black")
car_b = Car("Mustang",2023,"light blue")
print(car_a.model,car_a.year,car_a.color)
car_a.drive()
car_b.stop()
