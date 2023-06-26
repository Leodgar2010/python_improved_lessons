# Напишите функцию, которая открывает на чтение созданные
# в прошлых задачах файлы с числами и именами.
# Перемножьте пары чисел. В новый файл сохраните
# имя и произведение:
# если результат умножения отрицательный, сохраните имя
# записанное строчными буквами и произведение по модулю
# если результат умножения положительный, сохраните имя
# прописными буквами и произведение округлённое до целого.
# В результирующем файле должно быть столько же строк, сколько
# в более длинном файле. При достижении конца более короткого файла,
# возвращайтесь в его начало.
import typing
def read_per_line (file_obj:typing.TextIO):
    line = file_obj.readline()
    if line == "":
        file_obj.seek(0)
        line = file_obj.readline
    return line

def my_func(numbers, names, result):
    with (
        open(numbers, 'r', encoding='utf-8') as nums,
        open(names, 'r', encoding='utf-8') as nam,
        open(result, 'a', encoding='utf-8') as res
    ):
        len_names = sum(1 for _ in nam)
        len_numbers= sum(1 for _ in nums)
        for _ in range (max(len_names,len_numbers)):
            name = read_per_line(nam)
            num_line=read_per_line(nums)
            a= nums.split('|')
            # int_num, float_num = int(int_num),float(float_num)
            # print (int_num,float_num)
        # for i in nums:
        #     a= i.split('|')
        #     print (a)
        #     a = i.split("|")([0] * [1])
        # for i in names:
        #     b = nam.readlines()
        # if a < 0:
        #     a = abs(a)
        #     b = str(b).lower()
        # else:
        #     a = int(a)
        #     b = str(b).upper()
my_func('numbers.txt','names.txt','result.txt')