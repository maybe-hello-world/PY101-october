"""
My little Stack
"""
items = []

def push(elem) -> None:
	"""
	Operation that add element to stack

	:param elem: element to be pushed
	:return: Nothing
	"""
	items.append(elem)
	return None


def pop():
	"""
	Pop element from the top of the stack

	:return: popped element
	"""

	global items
	if items:
		return items.pop()
	else:
		return None

def peek(ind: int = 0):
	"""
	Allow you to see at the element in the stack without popping it

	:param ind: index of element (count from the top)
	:return: peeked element
	"""
	return items[len(items) - 1 - ind]


def clear() -> None:
	"""
	Clear my stack

	:return: None
	"""
	global items
	items = []
	return None
