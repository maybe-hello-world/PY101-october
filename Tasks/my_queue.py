"""
My little Queue
"""
Queue=[]

def enqueue(elem) -> None:
	global Queue
	"""
	Operation that add element to the end of the queue

	:param elem: element to be added
	:return: Nothing
	"""
	Queue.append(elem)
	return None


def dequeue():
	global Queue
	"""
	Return element from the beginning of the queue

	:return: dequeued element
	"""
	if len(Queue)<=0:
		return None
	else:
		deq=Queue[0]
		Queue=Queue[1:]
		return deq


def peek(ind: int = 0):
	global Queue
	"""
	Allow you to see at the element in the queue without dequeuing it

	:param ind: index of element (count from the beginning)
	:return: peeked element
	"""
	if len(Queue)>ind:
		return Queue[ind]
	else:
		return None


def clear() -> None:
	global Queue
	"""
	Clear my queue

	:return: None
	"""
	Queue=[]
	return None
