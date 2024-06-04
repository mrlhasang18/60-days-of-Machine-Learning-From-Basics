'''
Inheritance: A feature of OOP which allows a new class to inherit from an already existing class
'''
#parent class
class faculty:
    fac = input("Enter your faculty: ")
    
    def __init__(self,name,batch) -> None:
        self.name = name
        self.batch = batch
    
    #method to represent object as a string
    def __str__(self):
        return(
            f"{self.name } is from {self.fac} faculty {self.batch}th batch."
        )
        
#student class: child class
        
class student(faculty):  
    #student class inherits from faculty class
    pass 

a=input("Enter your name: ")
b=input("Enter your batch year: ")
lhasang = student(a,b)

print("-------- Student Info -------")
print(lhasang.batch)
print(lhasang)
print(lhasang.fac)

print(isinstance(lhasang,student))