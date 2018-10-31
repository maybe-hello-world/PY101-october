"""
My little Stack
"""
stack = []

def push(elem) -> None:
	"""
	Operation that add element to stack

	:param elem: element to be pushed
	:return: Nothing
	"""
	stack.append(elem)
	return


def pop():
	"""
	Pop element from the top of the stack

	:return: popped element
	"""
	if len(stack) > 0:
		a = stack[-1]
		del stack[-1]
		return a


def peek(ind: int = 0):
	"""
	Allow you to see at the element in the stack without popping it

	:param ind: index of element (count from the top)
	:return: peeked element
	"""
	return stack[-ind - 1]


def clear() -> None:
	"""
	Clear my stack

	:return: None
	"""
	del stack[:]
	return
