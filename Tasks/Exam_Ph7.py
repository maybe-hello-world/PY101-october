import random as rnd

n = 10**2
arr = [rnd.randint(1,6) for i in range(n)]
print(arr)

def sort(arr,left,right):
    length = (right-left)+1
    s = [0 for _ in range(length)]
    st = []
    for i in arr:
        s[i] += 1
    for i in range(length):
        for j in range(s[i]):
            st.append(i)
    return st

print(sort(arr,13,25))