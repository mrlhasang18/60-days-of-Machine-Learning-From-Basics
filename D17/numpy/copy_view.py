# copy and view in numpy

import numpy as np

a = np.array([2,4,5,6,7,8])

# create a view
print("-------- View ----------")
b = a.view()

print(f'original a: {a}')
print(f'original b: {b}')

a[2] = 3

print(f'Changed  a: {a}')
print(f'original b: {b}')

#create a copy
d = np.array([6,7,8,9,10])
print("-------- Copy ----------")
c = d.copy()

print(f'original d: {d}')
print(f'original c: {c}')

d[2] = 3

print(f'Changed  d: {d}')
print(f'original c: {c}')

# So in view both arrays are linked somehow and if one is changed then other is also changed
# whereas copy copys the values in different location which is not linked