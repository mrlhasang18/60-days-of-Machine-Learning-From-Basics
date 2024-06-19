# NumPy : numeric python. It is an alterntive to Python list: NumPy Array 
# It is a fundamental in Machine learning to learn
#  Datatype: ndarray: n-dimensional array
# lets do some calculations with at first

'''
a = [1,2,3]
b = [3,4,5]
c = (a+b) **2
print(c)
It will show a type error, and to overcome that we numpy array
'''

# Now let's use numpy array 

import numpy as np

a = np.array([1,2,3])
b = np.array([3,4,5])

print("Square of sum: ",(a+b)**2)

# shape: number of elements in numpy array
print(a.shape)  

# range
c = np.arange(6)
print("Arange: ",c)

# zeros
print("Single-dimensional zeros: \n",np.zeros(5))
print("Multi-dimensional zeros: \n",np.zeros((2,4)))

# Fulls
print("Multi-Dimensional Full: \n",np.full((2,4),18))

# Slicing 1d array
n = np.array([2,3,4,6,45])
print("Sliced: ",n[1:3])

# Slicing 2d array

m = np.array([[2,3,4],
              [5,6,7],
              [8,9,10]])
print("2d array slice:\n",m[1:3,1:3])

# steps on entire array
print("------ steps entire array -------")
z = np.array([0,1,2,3,4,5,6,7,8,9])
print(z[::2],z[::3])