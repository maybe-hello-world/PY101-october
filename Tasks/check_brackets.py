import Tasks.my_stack as mst

def check_brackets(brackets_row: str) -> bool:
    """
    Check whether input string is a valid bracket sequence

    :param brackets_row: input string to be checked
    :return: True if valid, False otherwise
    """
    mst.clear()
    for br in brackets_row:
        if br == "(":
            mst.push(br)
        else:
            if len(mst.my_st) == 0:
                return False
            else:
                mst.pop()
    return True if len(mst.my_st) == 0 else False
