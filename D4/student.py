import time

'''time has many time related functions like 
time.time(): to get the current time in seconds since the epoch
time.sleep(): to sleep certain amount of time
time.ctime(): to get the current local time
'''
def connect() -> None:
    print("Connecting to internet....")
    time.sleep(3)
    print("!! Connected succesfully !!")
    print(time.ctime())

class Student:
    #Attributes
    name = None
    roll = None
    gpa = None
    
    #constructor 
    def __init__(self,name,roll,gpa):
        self.name = name
        self.roll = roll
        self.gpa = gpa
        
    #Methods
    def pass_fail(self):
        if(self.gpa>=1.8):
            print(self.name+" has passed \n")
        else:
            print(self.name+" has failed \n")

#taking input from user
''''
a = str(input("Enter students name: "))
b = int(input("Enter roll: "))
c = float(input("Enter gpa: "))
ob = Student(a,b,c)
ob.pass_fail()

'''

'''if __name__ == '__main__': in a Python script, it’s a conditional statement that 
checks whether the current script is being run as the main program or being imported
as a module.'''

if __name__ == '__main__':
    connect()
    a = Student("lama",28,4.0)
    a.pass_fail()
