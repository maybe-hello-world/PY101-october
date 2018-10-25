queue = [[] for i in range(5)]

def enqueue(elem, priority: int = 0):
    queue[priority].append(elem)
    return

def dequeue():
    b = None
    for i in queue:
        if len(i) != 0:
            b = i.pop(0)
            break
        else:
            continue
    return b

def peek(ind: int = 0, priority: int = 0):
    return queue[priority][ind]

def clear():
    del queue[:]
    return
