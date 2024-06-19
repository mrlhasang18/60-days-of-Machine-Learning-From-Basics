# reshaping arrays in python

import numpy as np

# reshape() function is used to give a new shape to an array without changing its data

a = np.array([0,1,2,3,4,5,6,7,8,9,10,11])

# in 1d array
print(a)
print(a.shape)

# in 2d array
b = a.reshape(2,6)
print(b)
print(b.shape)

print(b.reshape(2,3,2))
print(b.shape)


# flatten to 1d
print(" --------- Flatten to 1D array ---------- ")
np1 = b.reshape(-1)
print(np1)
print(np1.shape)

# sorting in numpy array
print(" ---------- sorting in numpy array ------- ")
print(np.sort([2,1,4,3,8,45]))

# searching in numpy array
print(" ---------- searching in numpy array ------- ")
a = np.array([3,4,2,6,5])
print(np.where(a == 2))

# even numbers
print(np.where(a%2 == 0))

# filtering array
print(" ---------- filtering array ------- ")
filtered =[]
for i in a:
    if i%2 == 0:
        filtered.append(True)
    else:
        filtered.append(False)
        
print(a)
print(filtered)
print(a[filtered])