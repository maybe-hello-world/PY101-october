"""
My little Queue
"""
queue = []


def enqueue(elem) -> None:
	"""
	Operation that add element to the end of the queue

	:param elem: element to be added
	:return: Nothing
	"""
	queue.append(elem)
	return None


def dequeue():
	"""
	Return element from the beginning of the queue

	:return: dequeued element
	"""
	if len(queue) > 0:
		b = queue[0]
		del queue[0]
		return b
	# return None


def peek(ind: int = 0):
	"""
	Allow you to see at the element in the queue without dequeuing it

	:param ind: index of element (count from the beginning)
	:return: peeked element
	"""
	return queue[ind]
	# return None


def clear() -> None:
	"""
	Clear my queue

	:return: None
	"""
	del queue[:]
	return
	# return None
