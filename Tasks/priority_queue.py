"""
Priority Queue

Queue priorities are from 0 to 5
"""

items = [[], [], [], [], [], []]


def enqueue(elem, priority: int = 0) -> None:
	"""
	Operation that add element to the end of the queue

	:param elem: element to be added
	:return: Nothing
	"""
	items[priority].insert(0, elem)
	return None


def dequeue():
	"""
	Return element from the beginning of the queue

	:return: dequeued element
	"""

	global items
	for i in range(6):
	    if items[i]:
		    return items[i].pop()

	return None

def peek(ind: int = 0, priority: int = 0):
	"""
	Allow you to see at the element in the queue without dequeuing it

	:param ind: index of element (count from the beginning)
	:return: peeked element
	"""
	return items[priority][- 1 - ind]



def clear() -> None:
	"""
	Clear my queue

	:return: None
	"""

	global items
	items = [[], [], [], [], [], []]
	return None
