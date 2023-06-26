#  Напишите программу, которая вычисляет площадь
# круга и длину окружности по введённому диаметру.
# ✔ Диаметр не превышает 1000 у.е.
# ✔ Точность вычислений должна составлять
# не менее 42 знаков после запятой.
import math
import decimal

decimal.getcontext().prec = 42
while True:
    diameter = int(input("Введите диаметр: "))
    if 0 < diameter < 1000:
        break
print(f"Длина окружности: {decimal.Decimal(2 * math.pi * diameter / 2)}")
print(f"Площадь круга: {decimal.Decimal((math.pi * (diameter / 2)) ** 2)}")
