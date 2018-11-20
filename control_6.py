orders = [[1,5],[5,20],[20,23]]
time_line = [0]*24

def my_orders(orders):
    result = "Хватит"
    for i in range(len(orders)):
        hour = [x for x in range(orders[i][0], orders[i][-1])]
        for j in hour:
            if time_line[j] == 0:
                time_line[j] = 1
            else:
                return "Не хватит"
                break
    return result

print(my_orders(orders))