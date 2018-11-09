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
        i = 1
        j = 0
        result = np.zeros(len(prefix_str), dtype=int)
        while i != len(prefix_str):
            if prefix_str[i] == prefix_str[j]:
                result[i] = j + 1
                i += 1
                j += 1
            elif j == 0:
                result[i] = 0
                i += 1
            else:
                j = result[j - 1]

        return list(result)

    i = j = 0
    pfunc = prefix_fun(substr)
    print(type(pfunc),pfunc)
    if len(substr) == 0:
        return None
    m = len(inp_string)
    n = len(substr)
    while i != m and j < n:
        if inp_string[i] == substr[j]:
            i += 1
            j += 1
        elif j <= 0:
           i += 1
        elif j > 0:
            j = pfunc[j - 1]
    print(i,j)
    return i - len(substr) if j > 0 else None

