"""
My little Queue
"""
items = []

def enqueue(elem) -> None:
    """
    Operation that add element to the end of the queue

    :param elem: element to be added
    :return: Nothing
    """

    items.insert(0, elem)
    return None


def dequeue():
    """
    Return element from the beginning of the queue

    :return: dequeued element
    """

    global items
    if items:
        return items.pop()
    else:
        return None


def peek(ind: int = 0):
    """
    Allow you to see at the element in the queue without dequeuing it

    :param ind: index of element (count from the beginning)
    :return: peeked element
    """
    return items[len(items) - 1 - ind]


def clear() -> None:
    """
    Clear my queue

    :return: None
    """

    global items
    items = []
    return None
