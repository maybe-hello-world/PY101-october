"""
My little Queue
"""
my_qu = []

def enqueue(elem) -> None:
	"""
	Operation that add element to the end of the queue

	:param elem: element to be added
	:return: Nothing
	"""
	my_qu.append(elem)
	#return print("On stack! : ", my_qu)
	return None


def dequeue():
	"""
	Return element from the beginning of the queue

	:return: dequeued element
	"""
	if len(my_qu) == 0:
		return print("My_stack is empty")
	returned = my_qu.pop(0)
	#return print("It returns > %s < from queue" % returned)
	return returned


def peek(ind: int = 0):
	"""
	Allow you to see at the element in the queue without dequeuing it

	:param ind: index of element (count from the beginning)
	:return: peeked element
	"""
	if len(my_qu) == 0:
		return print("My_stack is empty")
	return my_qu[ind]


def clear() -> None:
	"""
	Clear my queue

	:return: None
	"""
	my_qu.clear()
	return None
