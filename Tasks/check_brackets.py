import Tasks.my_stack as my_stack

def check_brackets(brackets_row: str) -> bool:
    my_stack.clear()
    for b in brackets_row:
	    if b == '(':
		    my_stack.push(b)
	    elif b == ')':
		    if not my_stack.pop():
			    return False
    if my_stack.pop():
        return False
    else:
        return True


#print(check_brackets("(()))"))
#print(check_brackets("(()("))
#print(check_brackets("(()))"))
#print(check_brackets("(()))"))

