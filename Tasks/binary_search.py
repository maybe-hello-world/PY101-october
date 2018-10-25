import numpy as np
arr = np.array([i for i in range(100)] + [101])
#print(arr)


def binary_search_it(elem, arr):
    """
    Performs binary search of given element inside of array
    :param elem: element to be found
    :param arr: array where element is to be found
    :return: Index of element if it's presented in the arr, None otherwise
    """
    if elem not in arr:
        return None
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


def binary_search(elem, arr, left_b=0, right_b=-1):
    """
    Performs binary search of given element inside of array
    :param elem: element to be found
    :param arr: array where element is to be found
    :return: Index of element if it's presented in the arr, None otherwise
    """
    if elem not in arr:
        return None
    if right_b == -1:
        right_b = len(arr)
    half = (right_b + left_b) // 2
    if arr[half] < elem:
        return binary_search(elem, arr, left_b=half, right_b=right_b)
    else:
        return binary_search(elem, arr, left_b=left_b, right_b=half)



