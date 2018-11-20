arr = [5,3,4,11,2,9,7,21,6,20,19,8]


def b_sort(arr):
    for _ in range(len(arr)):
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr

# print(b_sort(arr))
#optimize_1 for second range: len(arr)-i
#optimeze_2 if no one sorts, stop algoritm


# def k_select(arr):

def merging(arr):
    def merge(arr_1,arr_2):
        i = j = 0
        arr = []
        while i < len(arr_1) and j < len(arr_2):
            if arr_1[i] < arr_2[j]:
                arr.append(arr_1[i])
                i+=1
        else:
                arr.append(arr_2[j])
                j+=1
        if i == len(arr_1):
            arr.extend(arr_2[j:])
        else:
            arr.extend(arr_1[i:])
        return arr

    if len(arr) == 1:
        return arr
    else:
        mid = len(arr) // 2
        arr_1 = arr[0:mid]
        arr_2 = arr[mid:]
    return merge(merging(arr_1),merging(arr_2))
print(merging(arr))

