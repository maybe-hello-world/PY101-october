#необходимо передавать левую и правую границы

def binary_search(elem, arr, left = 0, right = -1):
    """
    Performs binary search of given element inside of array
    :param elem: element to be found
    :param arr: array where element is to be found
    :return: Index of element if it's presented in the arr, None otherwise
    """
    if right == -1:
        right = len(arr)
    if elem < arr[0] or elem > arr[len(arr) - 1]:
        return None
    if left > right:
        return None
    else:
        mid = (right + left) // 2
        if arr[mid] == elem:
            return mid
        elif elem < arr[mid]:
            return binary_search(elem, arr, left, mid - 1)
        else:
            return binary_search(elem, arr, mid + 1, right)



arr = [i for i in range(100)] + [101]
print(binary_search(55, arr))





