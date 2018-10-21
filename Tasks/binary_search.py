import numpy as np
arr = np.array([i + 1 for i in range(1, 10)])
print(arr)


def binary_search(elem, arr):
	"""
	Performs binary search of given element inside of array

	:param elem: element to be found
	:param arr: array where element is to be found
	:return: Index of element if it's presented in the arr, None otherwise
	"""
	left = 0
	right = len(arr)
	half = 0

	while arr[half] != elem:
		half = (right + left) // 2
		if arr[half] < elem:
			left = half
		else:
			right = half
	return half

print(binary_search(5,arr))