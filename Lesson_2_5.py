print ('Введите коэффициенты квадратного уравнения:')
a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))

d = b ** 2 - 4 * a * c
# print (d)
# complex_number = -b + complex(0, math.sqrt(abs(d)))
# print (complex_number)
if d != 0:
    x1 = (-b + pow(d, 0.5)) / 2 / a
    x2 = (-b - pow(d, 0.5)) / 2 / a
    print("x1 = ", x1)
    print("x2 = ", x2)
else:
    x = -b / (2 * a)
    print("x = %.2f" % x)
