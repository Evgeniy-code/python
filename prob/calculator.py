#!/usr/bin/env python3 
a = float(input("введите первое число:"))
what = input("что делаем (+:-:*:/):")
b = float(input("введите второе число:"))
if what == "+":
    d = a + b
    print("равно:" + str(d))
elif what == "-":
    d = a - b
    print("равно:" + str(d))
elif what == "*":
    d = a * b
    print("равно:" + str(d))
elif what == "/":
    d = a / b
    print("равно:" + str(d))
else:
    print("введено неверное значение")
