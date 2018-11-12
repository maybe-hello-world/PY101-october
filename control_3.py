text = ['ATTA',
        'АCTA',
        'АGCA',
        'ACAA']

def common_letter(sl:list):
    """
    :param sl: list stolb
    :return:com:char
    """
    com = None
    di = {}
    for i in sl:
        if i in di.keys():
            di[i] += 1
        else:
            di[i] = 1

    m = max(di.values())

    for i, j in di.items():
        if j == m:
            com = i

    return com

def get_pos_str(text:list):
    res =[]
    for i in range(0,len(text)):
        st = [x[i] for x in text]
        res.append(common_letter(st))
    return res




print(get_pos_str(text))









