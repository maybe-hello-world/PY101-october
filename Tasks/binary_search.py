import numpy as np
arr = np.array([i for i in range(100)] + [101])


def binary_search_it(elem, arr, left_b = 0, right_b = -1):
    """
    Performs binary search of given element inside of array
    :param elem: element to be found
    :param arr: array where element is to be found
    :return: Index of element if it's presented in the arr, None otherwise
    """
    if right_b == -1:
        right_b = len(arr)
    half = (right_b + left_b) // 2
    if elem < 0:
        return None
    else:
        while arr[half] != elem and left_b <= right_b:
            half = (right_b + left_b) // 2
            if elem < arr[half]:
                right_b = half - 1
            else:
                left_b = half + 1
        return half if left_b <= right_b else None


def binary_search(elem, arr, left_b = 0, right_b = -1):
    """
    Performs binary search of given element inside of array
    :param elem: element to be found
    :param arr: array where element is to be found
    :return: Index of element if it's presented in the arr, None otherwise
    """
    if right_b == -1:
        right_b = len(arr)
    if left_b > right_b or elem < 0:
        return None
    else:
        half = (right_b + left_b) // 2
        if arr[half] == elem:
            return half
        elif elem < arr[half]:
            return binary_search(elem, arr, left_b, half - 1)
        else:
            return binary_search(elem, arr, half + 1, right_b)



