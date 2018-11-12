text = ['ATTA',
        'BCTA',
        'BGCA',
        'BCAA']

def common_letter(sl:list):
    """
    :param sl: list stolb
    :return:com:char
    """
    di = {}
    for i in sl:
        ke = i
        if ke in di.keys():
            di[ke] += 1
        else:
            di[ke] = 1
    m = max(di.values())

    for i, j in di.items():
        if j == m:
            return i

    return None

def get_pos_str(test:list):
    res =[]
    for i in range(0,len(text)):
        st = [x[i] for x in text]
        res.append(common_letter(st))
    return res




print(get_pos_str(text))









