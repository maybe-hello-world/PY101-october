"""
My little Stack
"""
my_st = []

def push(elem) -> None:
	"""
	Operation that add element to stack

	:param elem: element to be pushed
	:return: Nothing
	"""
	my_st.append(elem)
	#return print("On stack! : ", my_st)
	return None


def pop():
	"""
	Pop element from the top of the stack

	:return: popped element
	"""
	if len(my_st) == 0:
		return print("My_stack is empty")
	returned = my_st[-1]
	my_st.pop()
	#return print("It returns > %s < from stack" % returned)
	return returned


def peek(ind: int = 0):
	"""
	Allow you to see at the element in the stack without popping it

	:param ind: index of element (count from the top)
	:return: peeked element
	"""
	if len(my_st) == 0:
		return print("My_stack is empty")
	return my_st[- ind - 1]


def clear() -> None:
	"""
	Clear my stack

	:return: None
	"""
	my_st.clear()
	return None
