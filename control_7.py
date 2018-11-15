import random as rnd

mass = [rnd.randint(13,25) for i in range(10**2)]
print(mass)

def my_sort(arr,my_min,my_max):
    diap = (my_max - my_min) + 1
    s = [0 for _ in range(diap)]
    result = []
    for i in arr:
        s[i - diap] += 1
    for i in range(diap):
        for j in range(s[i]):
            result.append(i + diap)
    return result


print(my_sort(mass,13,25))

