from random import randint


def ugadayka(b):
    cheslo = randint(1, b)
    print('Добро пожаловать в числовую угадайку')


    def is_valid(n):
        return n.isdigit() and 1 <= int(n) <= b


    count = 0
    while True:
        count += 1
        print("Введите число от 1 до", b)
        s = input()
        if is_valid(s) == False:
            print('А может быть все-таки введем целое число от 1 до', b, '?')
            continue
        s = int(s)
        if s < cheslo:
            print('Ваше число меньше загаданного, попробуйте еще разок')
        elif s > cheslo:
            print('Ваше число больше загаданного, попробуйте еще разок')
        elif s == cheslo:
            print('Вы угадали, поздравляем!')
            print("Колличество попыток", count)
            if input("Сыграем еще раз? 'y' - 'да', 'n' - 'нет'") == 'y':
                print("До кокого максимального числа загадывать?")
                ugadayka(int(input()))
            else:
                print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
            break


ugadayka(100)


