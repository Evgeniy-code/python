def mac():
    from random import choice
    m = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F']
    mylist1 = [choice(m)] + [choice(m)]
    mylist2 = [choice(m)] + [choice(m)]
    mylist3 = [choice(m)] + [choice(m)]
    mylist4 = [choice(m)] + [choice(m)]
    mylist5 = [choice(m)] + [choice(m)]
    mylist6 = [choice(m)] + [choice(m)]
    return print(*mylist1 + [':'] + mylist2 + [':'] + mylist3 + [':'] + mylist4 + [':'] + mylist5 + [':'] + mylist6, sep='')


mac()
