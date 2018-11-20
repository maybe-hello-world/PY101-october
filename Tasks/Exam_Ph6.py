h = [0 for i in range(24)]

zayavka = [(1,4),(3,5),(4,6),(22,23),(4,8)]
# zayavka = [(1,3),(3,5),(22,23),(6,8)]

start = 1
end  = 2
def arenda(zayavka):
    for i,j in zayavka:
        for k in range(i,j):
            if h[k] == start:
                return False,"Rent is not possible!"
            else:
                h[k] = start

    return "Place the target!"


print(arenda(zayavka))