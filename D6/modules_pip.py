# Day 6 of learning Machine learning From the basics
# pip and  modules: the reason why python is one of the used is due to its pip and module feature
# which allows you to install and use libraries and modules from the internet.

# The pip command is used to install modules from the internet.
# pip install <module_name>   :
# To install numpy we can open terminal and type: pip install numpy
# To install pandas we can open terminal and type: pip install pandas

import pandas as p 
import numpy as np

#load file
students = p.read_csv('students - Sheet1.csv')
print("-------------- use of pandas ------------")
print(students.head())
#head function loads the first few rows of file

# Now let's use numpy: numeric python

# Create a numpy array
print("-------------- use of numpy ------------")
a = np.array([1,2,3,4,5])
b = np.array([2,5,6,3,1])
print("sum of a and b is :",a+b)
print(type(a+b))

# I will be exploring theses amazing modules in future soon, for now this is for just knowing about pip and modules


