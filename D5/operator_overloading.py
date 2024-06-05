# operator overloading in POOP
# Operator overloading is the feature that allows the sampe operator to have different meaning according to context
class a:
    
    def __init__(self,a,b,c) -> None:
          self.a = a
          self.b = b
          self.c = c
          
    def __str__(self) -> str:
         return f"{self.a} i + {self.b} j + {self.c} k"
    
    def __add__(self,d):
         
         return f"{self.a+d.a} i + {self.b+d.b} j + {self.c+d.c} k"
    
    def __sub__(self,d):
        return f"{self.a-d.a} i + {self.b-d.b} j + {self.c-d.c} k"
    
     
v1 = a(1,2,3)
print("v1 = ",v1)
v2 = a(2,3,4)
print("v2 = ",v2)
print("----Addition----\n",v1+v2)
print("----Substraction----\n",v1-v2)

