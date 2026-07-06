import numpy as np

array=np.array([1,2,3,4,5])


array_2d=np.array([
    [2,3,5],
    [2,4,6],
    [1,9,5]
]
)
print(array)
print("\n")
print(array_2d)
print("\n")
array_n=np.full((10,5), 10) #print 10,5 and all value 10

print(array_n)
print("\n")
add=array+2
print(add)
print("\n")

add_2d=array_2d+np.array([[2],[4],[3]]) #add row 2+ first row 4+ second row

print(add_2d)

print("\n")

print(np.shape(array_2d))

print("\n")

add_colum=array_2d+np.array([1,2,3]) #add column wise

print(add_colum)