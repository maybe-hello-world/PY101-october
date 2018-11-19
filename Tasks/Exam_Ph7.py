import random as rnd

n = 10**6
arr = [rnd.randint(13,25) for i in range(n)]
print(arr)

def sort(arr,left,right):
    length = (right-left)+1
    s = [0 for _ in range(length)]
    # print(s)
    st = []
    for i in arr:
        s[i-length] += 1
    # print(s)
    for i in range(length):
        for j in range(s[i]):
            st.append(i+length)
    return st

print(sort(arr,13,25))

# x = sort(arr,13,25)
# x = [rnd.randint(13,25) for i in range(n)]
# for i in x:
#     if x[i] > x[i+1]:
#         print("Array not sort")
#         break