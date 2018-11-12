arr = ['ATTA','ACTA','AGCA','ACAA']
n = len(arr[0])

def cs():
    key = {}
    consensus = []
    for i in range(n):
        for j in arr:
            stlb = j[i]
            # print(stlb)
            if stlb in j and stlb in key.keys():
                key[stlb]+=1
            else:
                key[stlb]=1
        maxim = max(key.values())
        for i,j in key.items():
            if j==maxim:
                consensus.append(i)
        key.clear()
    cons = ''.join(consensus)
    return cons
# print(key)
print(cs())
