queue = []

def enqueue(elem):
	queue.append(elem)
	return

def dequeue():
	if len(queue) > 0:
		b = queue[0]
		del queue[0]
		return b

def peek(ind: int = 0):
	return queue[ind]

def clear():
	del queue[:]
	return