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


		f = []

		for i in range(len(prefix_str)):
			j = i
			offset = 0
			while j > 0:
				j -= 1
				# print(i, j, offset, prefix_str[j], prefix_str[i-offset])
				if prefix_str[j] == prefix_str[i - offset]:
					offset += 1
				else:
					j += offset
					offset = 0
			f.append(offset)
			# print('append', offset)

		return f

	'''
		Важный Комментарий: первоначально был сделан вариант, который ищет не только первое, но и 
		последующие вхождения подстроки в строку и много тестовых выводов. Не удалял. 
		Поэтому в коде есть костыли и некоторая непричёсанность =) 		
	'''


	f = prefix_fun(substr)
	# print(f)

	i = 0
	j = 0
	done = False

	while not done:  # (input("Exit - 0") != '0')
		initf = False
		done = False

		a = inp_string[i:i + 1]
		b = substr[j:j + 1]
		# print('a=', a, 'b=', b)

		if a == b:
			i += 1
			j += 1
		elif j <= 0:
			i += 1
		else:
			j = f[j - 1]
		# print('i=', i, 'j=', j)
		# print(inp_string[:i])
		# print(substr[:j])

		if len(inp_string) == i:
			# print("Конец поиска : конец строки")
			done = True

		if len(substr) == j:
			# print("Подстрока найдена!", i - j)
			initf = True

			return i - j  # если закомментировать этот return, то будет искать последующие вхождеия

		if initf:
			i += 1
			j = 0

	return None


# res = KMP_algo('ATTATGGATGATCXATGATC', 'ATGATCZ')
# print(res)
