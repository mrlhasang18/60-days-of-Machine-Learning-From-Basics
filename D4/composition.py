'''
Composition: In POOP we use composition to combine classes to form a complex system
It is a technique where one class is composed of one or more instances of another classes
'''
class a:
    hashouse = None
    def __init__(self,hashouse) -> None:
        self.hashouse = hashouse
    
class b:
    la = None
    def __init__(self,la) -> None:
        self.la = la
    def homeless_not(self):
        if(self.la.hashouse == 'no'):
            print("Homeless")
        elif(self.la.hashouse == 'yes'):
            print("Has home")
        else:
            print("!!Invalid Input!!")

val = input("---------------\nIf you have a house enter 'yes' if not then enter 'no': ")
lhasang = b(a(val))
lhasang.homeless_not()