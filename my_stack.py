stack = []

def push(elem):
	stack.append(elem)
	# print(stack)
	return

def peek(ind: int = 0):
	# print(stack)
	return stack[-ind-1]

def pop():
	if len(stack) > 0:
		a = stack[-1]
		del stack[-1]
		return a

def clear():
	del stack[:]
	return