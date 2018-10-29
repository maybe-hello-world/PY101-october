'''

код нерабочий, заготовка

'''

f = [[[]]]
trace = []
Mx = 8
Ny = 10
prt = [0, 0]
cost = 1
procf = 2
metrica = 3
direct = 4


def init():
    global f
    f = [[[0, 0, 999999, 0] for _ in range(Mx)] for _ in range(Ny)]
    # [cost , procf, metrica, dir_in]
    # trace.append([0, 0])

def draw():
    global f
    print('\nFLD')
    for y in range(Ny):
        print(f[y], end='\n')



def step():
    def chkcell(x, offsetx, y, offsety):
        global f
        if offsetx > 1:
            offsetx = 1
        elif offsetx < -1:
            offsetx = -1
        elif offsety > 1:
            offsety = 1
        elif offsety < -1:
            offsety = -1

        if x + offsetx >= 0 and x + offsetx <= Mx and y + offsety >= 0 and y + offsety <= Ny:
            return f[x][y] + f[x + offsetx][y + offsety]
        else:
            return None


    for y in range(8):
        for x in range(8):
            chkcell(x, -2, y, -1)  # 9h
            chkcell(x, -1, y, -2)  # 7h
            chkcell(x, 1, y, -2)  # 5h
            chkcell(x, 2, y, -1)  # 3h

init()
# run()
f[ptr[0]][ptr[1]][1]
print(f[0][0][1])
draw()
