def count(n_people, k_syllable):
    i = 0
    while len(n_people) != 1:
        while k_syllable != 0:
            k_syllable -= 1
            i += 1
            if i == len(n_people):
                i = 0
            if k_syllable == 1:
                n_people.pop(i)
                k_syllable = 5
                if i == len(n_people):
                    i = 0
                break
    return n_people

print("last person number", count(n_people= [1, 2, 3, 4, 5, 6, 7], k_syllable=5))

