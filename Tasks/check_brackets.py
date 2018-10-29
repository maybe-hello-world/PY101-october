<<<<<<< HEAD
def check_brackets(stroka):
    st = []
    # if len(st) == 0: return True
    for i in stroka:
        if i == "(":
            st.append(i)
        else:
            if i == ")":
                if len(st) == 0: return False
                del st[-1]
            else:
                return False
    return not st
=======
def check_brackets(brackets_row: str) -> bool:
	"""
	Check whether input string is a valid bracket sequence

	:param brackets_row: input string to be checked
	:return: True if valid, False otherwise
	"""

	return False
>>>>>>> 0a10cd6c85aa9486d3350e979e6bd177e77e78e6
