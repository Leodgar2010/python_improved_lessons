# ✔ Создайте функцию-генератор.
# ✔ Функция генерирует N простых чисел,
# начиная с числа 2.
# ✔ Для проверки числа на простоту используйте
# правило: «число является простым, если делится
# нацело только на единицу и на себя»
n = 10

def check_simple(number):
    if number % 2 ==0 and number !=2:
        return False
    else:
        for i in range (3, int(number**0.5)+1,2):
            if number % i == 0:
                return False
        return True

def gen_simple_number(n):
    count =0
    yield 2
    number =3
    while count <n-1:
        if check_simple (number):
            yield number
            count +=1
        number+=2

print(*gen_simple_number(n))
