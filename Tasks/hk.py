f = [[]]

def init():
    global f
    f = [[0 for _ in range(8)] for _ in range(8)]
    f[0][0] = 1

def draw():
    global f
    print('\nF')
    for y in range(8):
        print(f[y], end='\n')



def run():
    def chkcell(x, offsetx, y, offsety):
        global f
        if x + offsetx >= 0 and x + offsetx <= 7 and y + offsety >= 0 and y + offsety <= 7:
            f[x][y] += f[x + offsetx][y + offsety]

    for y in range(8):
        for x in range(8):
            chkcell(x, -2, y, -1)  # 9h
            chkcell(x, -1, y, -2)  # 7h
            chkcell(x, 1, y, -2)  # 5h
            chkcell(x, 2, y, -1)  # 3h

init()
run()
draw()
