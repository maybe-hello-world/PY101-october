"""
Priority Queue

Queue priorities are from 0 to 5
"""


queue = [][]


def enqueue(elem, priority: int = 0) -> None:
    """
    Operation that add element to the end of the queue

    :param elem: element to be added
    :return: Nothing
    """

    global queue

    queue[priority][:0] = [elem]

    return None


def dequeue():
    """
    Return element from the beginning of the queue

    :return: dequeued element
    """

    global queue

    if len(queue) == 0:
        return None

    res = queue[len(queue) - 1]
    queue = queue[:-1]

    return None


def peek(ind: int = 0, priority: int = 0):
    """
    Allow you to see at the element in the queue without dequeuing it

    :param ind: index of element (count from the beginning)
    :return: peeked element
    """
    return None


def clear() -> None:
    """
    Clear my queue

    :return: None
    """
    return None
