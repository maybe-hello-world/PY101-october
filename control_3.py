text = ['ATTA',
        'ACTA',
        'AGCA',
        'ACAA',]

def common_letter(sl:list):
    """
    :param sl: list stolb
    :return:com:char
    """
    com = None
    di = {}
    di_sorted = {}
    for i in sl:
        if i in di.keys():
            di[i] += 1
        else:
            di[i] = 1

    m = max(di.values())

    for k in sorted(di.keys(),reverse=True):
        di_sorted[k] = di[k]

    for i, j in di_sorted.items():
        if j == m:
            com = i
    return com


def get_pos_str(text:list):
    res =[]
    j = 0
    for i in range(len(text)):
        while j < len(text[i]):
            st = [x[j] for x in text]
            j+=1
            res.append(common_letter(st))
    return res


print(get_pos_str(text))

