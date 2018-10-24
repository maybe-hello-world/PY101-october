f = [[]]
cou = [[]]

def init():
    global f
    global cou
    f = [[0 for _ in range(8)] for _ in range(8)]
    f[0][0] = 1
    cou = [[0 for _ in range(8)] for _ in range(8)]
    cou[0][0] = 1

def draw(df=True, dc=True):
    global f
    global cou
    print('\nF')
    if df:
        for y in range(8):
            print(f[y], end='\n')

    print('\nCOU')
    if dc:
        for y in range(8):
            print(cou[y], end='\n')

def hk(x, y, itern):
    def writeit(xi, yi):
        global f
        global cou
        if xi >= 0 and xi <= 7 and yi >= 0 and yi <= 7:
            if f[xi][yi] != 0:
                # print("@@@", xi, yi)
                pass

            f[xi][yi] = itern + 1
            res.append([xi, yi])


            cou[xi][yi] += 1 # сумма путей из предыдущей+


    res = []
    writeit(x-2, y+1)  # 9h
    writeit(x-1, y+2)  # 11h
    writeit(x+1, y+2)  # 1h
    writeit(x+2, y+1)  # 3h

    return res

def scanf(itern):
    isMove = False
    for yy in range(8):
        for xx in range(8):
            if f[xx][yy] == itern:
                hk(xx, yy, itern)
                print(itern, xx, yy, f[xx][yy])
                isMove = True

    return isMove

init()
itern = 1
hk(0, 0, itern)


while True:
    itern += 1

    ret= scanf(itern)
    draw()
    if ret:
        if input("Press Enter for next / 0 - Exit") == '0':
            break
    else:
        print('ЭТО ПОСЛЕДНЯЯ ВОЗМОЖНАЯ ИТЕРАЦИЯ')
        break

#draw('cou')