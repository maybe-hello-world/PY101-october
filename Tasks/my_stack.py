"""
My little Stack
"""
Stack = [1,2,3]

def push(elem) -> None:
	global Stack
	"""
	Operation that add element to stack

	:param elem: element to be pushed
	:return: Nothing
	"""
	Stack=[elem]+Stack
	#Stack.append(elem)
	return None


def pop():
	global Stack
	"""
	Pop element from the top of the stack

	:return: popped element
	"""
	if len(Stack)>0:
		poped=Stack[0]
		Stack=Stack[1:]
		return poped
	else:
		return None



def peek(ind: int = 0):
	global Stack
	"""
	Allow you to see at the element in the stack without popping it

	:param ind: index of element (count from the top)
	:return: peeked element
	"""
	if ind<len(Stack):
		return Stack[ind]
	else: return None


def clear() -> None:
	global Stack
	"""
	Clear my stack

	:return: None
	"""
	Stack=[]
	return None


