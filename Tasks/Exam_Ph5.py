from collections import Counter
# arr = ['ATTA','ACTA','AGCA','ACAA']
arr = ['AGTA','ACTA','AGCA','ACAA']
n = len(arr[0])
counter = 0

def cs():
    key = {}
    invertkey = {}
    consensus = []
    cnt=1
    for i in range(n):
        for j in arr:
            stlb = j[i]
            # print(stlb)
            if stlb in j and stlb in key.keys():
                key[stlb]+=1
            else:
                key[stlb]=1
        maxim = max(key.values())
        # for i,j in key.items():
        #     if j==maxim:
        #         consensus.append(i)
        for i,j in key.items():
            if j in invertkey:
                invertkey[j].join(i)
            else:
                invertkey[j] = i
                if j==maxim:
                    consensus.append(i)
            print(invertkey)
        key.clear()
        invertkey.clear()
    cons = ''.join(consensus)
    return cons
# print(key)
print(cs())
