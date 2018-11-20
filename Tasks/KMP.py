import numpy as np


def KMP_algo(inp_string: str, substr: str):
	"""
	Implementation of Knuth-Morrison-Pratt algorithm

	:param inp_string: String where substr is to be found (haystack)
	:param substr: substr to be found in inp_string (needle)
	:return: index where first occurrence of substr in inp_string started or None if not found
	"""

	def prefix_fun(prefix_str: str) -> list:
		"""
		Prefix function for KMP

		:param prefix_str: dubstring for prefix function
		:return: prefix values table
		"""
		i = 0
		j = 0
		for i in range(len(1,len(prefix_str))):
			if prefix_str[i] == prefix_str[j]:
				prefix_str[i] = j + 1
				i += 1
				j += 1
			elif j == 0:
				prefix_str[i] = 0
				i += 1
			else:
				j = prefix_str[j-1]
		return list(prefix_str)

	i, j = 0, 0
	prf = prefix_fun(substr)
	if inp_string[i] == prf[j]:
		i += 1
		j += 1
	elif j <= 0:
		i += 1

	elif j > 0:
		j = prf(j - 1)

	return None

str = "ATGATC"
def prefix_fun(prefix_str: str) -> list:
	"""
	Prefix function for KMP

	:param prefix_str: dubstring for prefix function
	:return: prefix values table
	"""
	key = np.array([0 for i in range(len(prefix_str))])
	i = 0
	j = 1
	while i != len(prefix_str):
		if key[i] == prefix_str[j]:
			key[i] = j + 1
			i += 1
			j += 1
		elif j == 0:
			key[i] = 0
			i += 1
		else:
			j = key[j - 1]
	return list(key)
print(prefix_fun(str))