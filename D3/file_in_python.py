#Day 3 of learning ML from basics

#Today at first we will be learning about how to work with files in python

print("\n----------- Working with files in Python -----------\n")

#creating and writing in file using write() function with mode 'w'

file = open('file.txt','w')     
#it can be also written as: with open('file.txt','w') as file:
file.write("Hello, this is me lhasang")    
print(file)
file.close()

#reading contents from file

file = open('file.txt','r')
fcontent = file.read()
print(fcontent)
file.close()

#adding additional info in file

file = open('file.txt','a')
file.write("\nI am learning python")
print("------- after appending -------")

#let's read our file after appending
file = open("file.txt",'r')
content=file.read()
print(content)
file.close()

#working with binary files
print("\n----------- Working with binary files in Python -----------\n")

#creating and writing in binary file
print("------ Writing ------")
bfile = open("python.webp",'wb')
bfile.write(b"Hello opened in binary mode")
print(bfile)
bfile.close()

#reading in binary mode

bfile = open("python.webp",'rb')
bcontent = bfile.read()

print(bcontent)
bfile.close()

#append in binary file

bfile = open("python.webp",'ab')
bfile.write(b' + this is after appended')
bfile = open("python.webp","rb")
print(bfile.read())
bfile.close()

#working with csv: (comma separated values) files
print("\n----------- Working with csv files in Python -----------\n")

import csv #importing csv

#creating csv file
file = open("example.csv","w",newline='')
a = csv.writer(file)
a.writerow(['Name: ','Lhasang'])
print(file)
file.close()

#reading csv file
file = open("example.csv","r")
c = csv.reader(file)
for i in c:
    print(i)
file.close()

