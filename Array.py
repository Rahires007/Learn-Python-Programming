#Array program
'''
Array :- Array is collection of homogeneous and hetrogeneous datatypes value store in contigeous memory 
Array index always start with 0 
Array s faster than list & tuple because of contigeous memory allocation
We cant create array directly in python we have to use numpy library for array 
'''
import numpy as np
Numbers=np.array([1,2,3,4,5])
print(type(Numbers))
print(Numbers)
print(Numbers.sum()) #Sum of array element
print(Numbers.min(),Numbers.max()) #Min & Max 
print(dir(Numbers)) #Check All supported array methods 