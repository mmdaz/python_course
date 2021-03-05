import numpy as np

#
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

two_d_array = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

new_two_d_array = two_d_array.copy()

view_two_d_array = two_d_array.view()

two_d_array[0] = [5, 4, 3, 2, 1]

print(two_d_array)
print(new_two_d_array)
print(view_two_d_array)
print(two_d_array)
print(two_d_array[0, 1])
print(two_d_array[1, 1:4])
print(two_d_array[:2, 2])
print(two_d_array[0:2, 1:4])

print(two_d_array.dtype)

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

new_arr = arr.reshape(4, 3)

print(new_arr)
