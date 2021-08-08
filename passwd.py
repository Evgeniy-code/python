from random import choice


def generate_password(a, b):
    passw = ''
    for _ in range(a):
        passw += choice(b)
    return passw


digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ''

print('Введите число, сколько паролей будем генерировать')
q = int(input())

print('Введите длинну пороля')
len_passwd = int(input())

print('Включать ли цифры 0123456789? "y" или "n"')
digit_passwd = input()
if digit_passwd == 'y':
    chars += digits


print('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ?  "y" или "n"')
upper_passwd = input()
if upper_passwd == 'y':
    chars += uppercase_letters

print('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? "y" или "n"')
lower_passwd = input()
if lower_passwd == 'y':
    chars += lowercase_letters

print('Включать ли символы !#$%&*+-=?@^_? "y" или "n"')
punctuation_passwd = input()
if punctuation_passwd == 'y':
    chars += punctuation

print('Исключать ли неоднозначные символы il1Lo0O? "y" или "n"')
iskl_passwd = input()
if iskl_passwd == 'y':
    for i in 'il1Lo0O':
        chars = chars.replace(i, '')

for _ in range(q):
    print(generate_password(len_passwd, chars))