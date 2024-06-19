print(" ----------- Universal functions in NumPy ------------")


#Universal Functions, or uFuncs, allow you to quickly do things to the elements of your Numpy Array

import numpy as np

# Universal functions in NumPy
a = np.array([-3,-2,-1,0,1,2,3,4,5])
print(a)

# min/max
print(np.max(a),np.min(a))

# square root of each elements
#print(np.sqrt(a))

# absolute 
print(np.abs(a))

# sign
print(np.sign(a))

# Trigonometry 
print(np.sin(a))
