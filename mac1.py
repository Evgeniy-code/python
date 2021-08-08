def binary(number):
    if number == 0:
        return print(0)
    result = ''
    while number > 0:
        modulo = number % 2
        result = str(modulo) + result
        number = number // 2
    if number == 0:
        return print(result)


binary(0)