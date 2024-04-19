import numpy as np

arr=np.array([1,2,3,4,5,6])

print(arr)
print(type(arr))

arr1 = np.zeros((3,7))
print(arr1)

arr2= np.ones((4,2))
print(arr2)

arr3= np.zeros((3,4)) + 10
print(arr3)

arr4 = np.arange(10, 100, 5)
print(arr4)

arr5 = np.arange(50, 100)
print(arr5)

arr6 = np.arange(15)
print(arr6)

arr7 = np.arange(18).reshape(3, 6)
print(arr7)
print(arr7.ndim)
print(arr7.shape)
print(arr7.size)
print(arr7.dtype)
print('-------------------------')

arr8 = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [40, 41, 42]]])
print(arr8)
print(arr8.ndim)
print(arr8.shape)
print(arr8.size)
print(arr7.dtype)
print('------------------------')

arr9 = np.array([[[13, 14, 15, 16], [17, 18, 19, 20], [80, 81, 82, 83]], 
                 [[21, 22, 23, 24], [25, 26, 27, 28], [84, 85, 86, 87]],
                 [[29, 30, 31, 32], [33, 34, 35, 36], [88, 89, 90, 91]]])
print(arr9)
print(arr9.ndim)
print(arr9.shape)
print(arr9.size)
print(arr7.dtype)
print('-----------------------')

arr10 = np.array([105, 106, 107, 108], np.uint8)
print(arr10.dtype)







