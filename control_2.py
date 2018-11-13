def shift(l, n):
    return l[n:] + l[:n]


people = [1,2,3,4]
k = 4
new_index = 0

def people_count(people,k):
    while len(people) > 1:
        if len(people) == 1:
            print (people[0])
        else:
            if len(people) >= k:
                new_index = k
            else:
                if k / len(people) == 0:
                    new_index = len(people)
                else:
                    new_index = k % len(people)
        #print("before shift",people)
        #print(new_index)
        people.remove(people[new_index - 1])
        people = shift(people,new_index - 1)
        #print("after shift",people)
    return people


print(people_count(people,k))
