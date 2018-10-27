import numpy as np
a = np.array([i**2 for i in range(1,10)])
def binary_search(elem, arr):
    left1=0
    right1=len(arr)-1
    mid=(left1+right1)//2
    while arr[mid]!=elem and left1<=right1 :
        if elem<arr[mid]:
            right1=mid-1
        else:
            left1=mid+1
        mid=(left1+right1)//2
    return mid if left1<=right1 else None
    #return None
#print(binary_search(16,a))
