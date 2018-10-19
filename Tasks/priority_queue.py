"""
Priority Queue

Queue priorities are from 0 to 5
"""


queue = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}


def enqueue(elem, priority: int = 0) -> None:
    """
    Operation that add element to the end of the queue

    :param elem: element to be added
    :return: Nothing
    """

    global queue

    # queue[priority][:0] = [elem]
    queue[priority].insert(0, elem)

    return None


def dequeue():
    """
    Return element from the beginning of the queue

    :return: dequeued element
    """

    global queue

    for iq in range(5):
        if len(queue[iq]) == 0:
            return None

        res = queue[iq][len(queue[iq]) - 1]
        queue[iq] = queue[iq][:-1]
        return res

    return None


def peek(ind: int = 0, priority: int = 0):
    """
    Allow you to see at the element in the queue without dequeuing it

    :param ind: index of element (count from the beginning)
    :return: peeked element
    """

    # ret = queue[priority][len(queue[priority]) - 1 - ind]

    return queue[priority][-1-ind]


def clear() -> None:
    """
    Clear my queue

    :return: None
    """

    for iq in range(5):
        queue[iq] = []

    return None
