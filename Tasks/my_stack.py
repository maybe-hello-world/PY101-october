"""
My little Stack
"""

stack=[]
def push(elem)-> None:
	"""
	Operation that add element to stack

	:param elem: element to be pushed
	:return: Nothing
	"""
	stack.append(elem)
	print(stack)
	return None


def pop():
	"""
	Pop element from the top of the stack

	:return: popped element
	"""
	if stack != []:
		top=stack[-1]
		stack.remove(stack[-1])
		print(stack)
		return top
	else:
		print("Стек пуст")
	return None


def peek(ind: int = 0):
	"""
	Allow you to see at the element in the stack without popping it

	:param ind: index of element (count from the top)
	:return: peeked element
	"""
	top=stack[-1-ind]
	return top


def clear() -> None:
	"""
	Clear my stack

	:return: None
	"""
	del stack[:]
	return None
