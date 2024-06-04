''' mutable vs Immutable

->mutable: can be changed
    dictionary is mutable
    list is mutable
    set is mutable
    
->immutable: cannot be changed
    str,int,float,bool,bytes,tuple are immutable

'''

#let's look at the mutable
print("\n----Mutables----- ")
#list
lama = [2,3]
print("\n1.List: \nList Before: ",lama)
lama.append(4)
print("List after: ",lama) 

#set
a={1,4,"apple"}
print("\n2.set: \nset Before: ",a)
a.add("cow")
print("set after: ",a)

#dictionary
d={"class":"python","time":"7:00AM"}
print("\n3.Dictionary: \nDict Before: ",d)
d["teacher"] = "Jerry lin"
print("Dict after: ",d)


#let's look at the immutables
print("\n----Immutables----- \n1.string\n2.Tuoles\n3.int\n4.float and other datatypes like bool")

'''
1.string
name = "lhasang"
name[1]= "b"
print(name)   ->shows type error since str(string) is immutable

2.Tuples

r= (1,4,5)
del(r[1])
print(r) 

and likewise other datatypes like int,float and bool also are immutable
'''
