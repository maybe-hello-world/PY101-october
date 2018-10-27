def check_brackets(brackets_row: str='') -> bool:
	#str=""
	"""
	Check whether input string is a valid bracket sequence

	:param brackets_row: input string to be checked
	:return: True if valid, False otherwise
	"""

	while '()' in brackets_row or '[]' in brackets_row or '{}' in brackets_row:
		brackets_row=brackets_row.replace('()','')
		brackets_row=brackets_row.replace('{}','')
		brackets_row=brackets_row.replace('[]','')
		#return True
	return not brackets_row
	#return not brackets_row
