"""
Priority Queue

Queue priorities are from 0 to 5
"""
queue = [[] for i in range(6)]


def enqueue(elem, priority: int = 0) -> None:
	"""
	Operation that add element to the end of the queue

	:param elem: element to be added
	:return: Nothing
	"""
	queue[priority].append(elem)
	return None


def dequeue():
	"""
	Return element from the beginning of the queue

	:return: dequeued element
	"""
	b = None
	for i in queue:
		if len(i) != 0:
			b = i.pop(0)
			break
		else:
			continue
	return b


def peek(ind: int = 0, priority: int = 0):
	"""
	Allow you to see at the element in the queue without dequeuing it

	:param ind: index of element (count from the beginning)
	:return: peeked element
	"""
	return queue[priority][ind]


def clear() -> None:
	"""
	Clear my queue

	:return: None
	"""
	for i in queue:
		i.clear()
	return None
