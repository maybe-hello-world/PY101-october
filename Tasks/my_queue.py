"""
My little Queue
"""

queue=[]
def enqueue(elem) -> None:
	"""
	Operation that add element to the end of the queue

	:param elem: element to be added
	:return: Nothing
	"""
	queue.append(elem)
	print(queue)
	return None



def dequeue():
	"""
	Return element from the beginning of the queue

	:return: dequeued element
	"""
	if queue != []:
		head=queue[0]
		queue.remove(queue[0])
		print(queue)
		return head
	else:
		print("Очередь пуста")
	return None


def peek(ind: int = 0):
	"""
	Allow you to see at the element in the queue without dequeuing it

	:param ind: index of element (count from the beginning)
	:return: peeked element
	"""
	head=queue[ind]
	return head


def clear() -> None:
	"""
	Clear my queue

	:return: None
	"""
	del queue[:]
	return None
