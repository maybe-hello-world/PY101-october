"""
My little Stack
v2
"""

stack = []

def push(elem) -> None:
	"""
	Operation that add element to stack

	:param elem: element to be pushed
	:return: Nothing
	"""
	global stack
	stack[:0] = [elem]
	return None


def pop():
	"""
	Pop element from the top of the stack

	:return: popped element
	"""
	global stack
	if len(stack) == 0:
		return None
	res = stack[0]
	stack = stack[1:]
	return res


def peek(ind: int = 0):
	"""
	Allow you to see at the element in the stack without popping it

	:param ind: index of element (count from the top)
	:return: peeked element
	"""
	return stack[ind]


def clear() -> None:
	"""
	Clear my stack

	:return: None
	"""
	global stack
	stack = []
	return None



