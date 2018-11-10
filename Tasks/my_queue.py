"""
My little Queue
"""

my_enqueue = []

def enqueue(elem) -> None:
	my_enqueue.append(elem)
	"""
	Operation that add element to the end of the queue

	:param elem: element to be added
	:return: Nothing
	"""
	return None


def dequeue():
	global my_enqueue

	if my_enqueue == []:
		return None
	else:
		deq_elem = my_enqueue[0]
		my_enqueue = my_enqueue[1:]
		return deq_elem

	"""
	Return element from the beginning of the queue

	:return: dequeued element
	"""


def peek(ind: int = 0):
	if my_enqueue == []:
		return None
	else:
		return my_enqueue[ind]
	"""
	Allow you to see at the element in the queue without dequeuing it

	:param ind: index of element (count from the beginning)
	:return: peeked element
	"""
	return None


def clear() -> None:
	my_enqueue.clear()
	"""
	Clear my queue

	:return: None
	"""
	return None
