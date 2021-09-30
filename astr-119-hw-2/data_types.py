import numpy as np #import numpy library

#integers

i = 10
print(type(i))

a_i = np.zeros(i, dtype=int) #declare an array of integers
print(type(a_i)) #will return ndarray
print(type(a_i[0])) #this will return int64

#floats
x = 119.0
print(type(x)) #print out the type of x

y = 1.19e2 #float 119 in scientific notation
print(type(y))

z = np.zeros(i, dtype=float) #declares array of floats
print(type(z)) #print type of array
print(type(z[0])) #float

