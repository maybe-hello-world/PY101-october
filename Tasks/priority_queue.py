"""
Priority Queue

Queue priorities are from 0 to 5
"""

my_pri_qu = [[] for i in range(6)]

def enqueue(elem, priority: int = 0) -> None:
	"""
	Operation that add element to the end of the queue

	:param elem: element to be added
	:return: Nothing
	"""
	"""
	if priority == 0:
		my_pri_qu[0].append(elem)
	elif priority == 1:
		my_pri_qu[1].append(elem)
	elif priority == 2:
		my_pri_qu[2].append(elem)
	elif priority == 3:
		my_pri_qu[3].append(elem)
	elif priority == 4:
		my_pri_qu[4].append(elem)
	elif priority == 5:
		my_pri_qu[5].append(elem)
	"""

	my_pri_qu[priority].append(elem)
	return None


def dequeue():
	"""
	Return element from the beginning of the queue

	:return: dequeued element
	"""
	returned = None
	for i in range(len(my_pri_qu)):
		if len(my_pri_qu[i]) == 0:
			continue
		returned = my_pri_qu[i].pop(0)
		break

	return returned


def peek(ind: int = 0, priority: int = 0):
	"""
	Allow you to see at the element in the queue without dequeuing it

	:param ind: index of element (count from the beginning)
	:return: peeked element
	"""
	if len(my_pri_qu[priority]) == 0:
		return print("My_stack is empty")
	return my_pri_qu[priority][ind]


def clear() -> None:
    """
    Clear my queue

    :return: None
    """
    for i in my_pri_qu:
        i.clear()

    return None
