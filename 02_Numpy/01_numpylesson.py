import numpy as np   #used for import numpy

arr=np.array([1,2,3,4,5])   # making numpy array
print(arr)     #printing arr
print(type(arr)) #print arr type

zeros=np.zeros(5)   #adding zeros
ones=np.ones(5)     #adding onces

range_arr=np.arange(1,11)  #making range
print(range_arr) #printing range

arr2=np.array([10,20,30,40,50])     #making arr for indexing and slicling

print(arr[0])
print(arr[-1])
print(arr[1:4])

matrix=np.array([[1,2,3],[4,5,6]])    #making 2D array for indexing and slicling

print(matrix[0])
print(matrix[1][2])
print(matrix[:,0])
print(matrix.ndim)
print(matrix.size)


my_list=np.array([1,2,3,4,5])
result=my_list+10
print(result)
print(my_list*2)
print(my_list**2)
print(my_list/2)
print(np.max(my_list))
print(np.min(my_list))
print(np.mean(my_list))
print(np.sum(my_list))
print(np.sort(my_list))
print(my_list.ndim)

a=np.array([1,2,3])
b=np.array([10,20,30])
print(a+b)

