"""
My little Stack
"""

my_stack = []
def push(elem) -> None:
	my_stack.append(elem)
	"""
	Operation that add element to stack

	:param elem: element to be pushed
	:return: Nothing
	"""
	return None


def pop():
	if my_stack == []:
		return None
	else:
		elem = my_stack.pop()
	"""
	Pop element from the top of the stack

	:return: popped element
	"""
	return elem


def peek(ind: int = 0):
	if my_stack == []:
		return None
	else:
		peek_elem = my_stack[-1-ind]
	"""
	Allow you to see at the element in the stack without popping it

	:param ind: index of element (count from the top)
	:return: peeked element
	"""
	return peek_elem


def clear() -> None:
	my_stack.clear()
	"""
	Clear my stack

	:return: None
	"""
	return None
