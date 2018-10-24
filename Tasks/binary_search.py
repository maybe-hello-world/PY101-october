def binary_search(elem, arr):
<<<<<<< HEAD
    local_mid = len(arr) // 2
    if elem == arr[local_mid]:
        print("элемент найден по индексу: ", local_mid)
        return local_mid
    elif len(arr) == 1:
        return None
    elif elem > arr[local_mid]:
        arr1 = arr[local_mid:]
        return search(arr1, elem, local_mid, False)
    elif elem < arr[local_mid]:
        arr2 = arr[:local_mid]
        return search(arr2, elem, local_mid, True)




def search(arr, elem, global_mid, left):
    local_mid = len(arr) // 2
    if left:
        global_mid = global_mid - len(arr) + local_mid
    else:
        global_mid = global_mid + local_mid
    if elem == arr[local_mid]:
        print("элемент найден по индексу: ", global_mid)
        return global_mid
    elif len(arr) == 1:
        return None
    elif elem > arr[local_mid]:
        arr1 = arr[local_mid:]
        return search(arr1, elem, global_mid, False)
    elif elem < arr[local_mid]:
        arr2 = arr[:local_mid]
        return search(arr2, elem, global_mid, True)
=======
	"""
	Performs binary search of given element inside of array

	:param elem: element to be found
	:param arr: array where element is to be found
	:return: Index of element if it's presented in the arr, None otherwise
	"""

	return None
>>>>>>> 0a10cd6c85aa9486d3350e979e6bd177e77e78e6
