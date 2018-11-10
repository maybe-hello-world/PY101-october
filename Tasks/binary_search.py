# Вариант1 - возвращает элемент из порезанного массива
def binary_search(elem, arr):
    if arr[-1]<=arr[0]:
        return None
    mid = len(arr)//2
    if arr[mid] > elem:
        return binary_search(elem, arr[0:mid-1])
    elif arr[mid] < elem:
        return binary_search(elem, arr[mid+1:])
    else:
        return mid

# print(binary_search(elem =89 , arr = [1, 4, 7, 15, 67, 89]))

"""
	Performs binary search of given element inside of array

	:param elem: element to be found
	:param arr: array where element is to be found
	:return: Index of element if it's presented in the arr, None otherwise
	"""
# Вариант2 - возвращает правильно элемент
def binary_search1(elem, arr, lo, hi):
    if hi<=lo:
        return None
    mid = (hi+lo)//2
    if arr[mid] > elem:
        return binary_search1(elem, arr, lo, mid)
    elif arr[mid]< elem:
        return binary_search1(elem, arr, mid+1, hi)
    else:
        return mid
#
print(binary_search1(elem =89 , arr = [1, 4, 7, 15, 67, 89], hi = 6, lo = 0))