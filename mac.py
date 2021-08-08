def mac():
    import random
    c = 'ABCDEF'
    b = 'ECBFAD'
    d = ''.join((random.choice(c) for i in range(1)))
    a1 = random.randrange(10, 99)
    a2 = d + str(random.randrange(10))
    a3 = ''.join((random.choice(b) for i in range(2)))
    a4 = random.randrange(10, 50)
    a5 = random.randrange(27, 84)
    a6 = str(random.randrange(10)) + ''.join((random.choice(c) for i in range(1)))
    return str(a1) + ":" + str(a2) + ":" + str(a3) + ":" + str(a4) + ":" + str(a5) + ":" + str(a6)


print(mac())