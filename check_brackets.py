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