#  Выведите в консоль таблицу умножения
# от 2х2 до 9х10 как на школьной тетрадке.
# ✔ Таблицу создайте в виде однострочного
# генератора, где каждый элемент генератора —
# отдельный пример таблицы умножения.
# ✔ Для вывода результата используйте «принт»
# без перехода на новую строку.
table_shape = [[2, 3, 4, 5], [6, 7, 8, 9]]
len_row = len(table_shape[0]) + len(table_shape[1])
FIRST_NUMBER = 2
LAST_NUMBER = 10
print(f"\n{'Т А Б Л И Ц А  У М Н О Ж Е Н И Я':>45}\n")

def my_gen(table_shape):
    for a in table_shape:
        # if a != 0:
        #      yield ('')
        for b in range(FIRST_NUMBER, LAST_NUMBER + 1):
            for k in range(0, len(table_shape[0])):
                yield (f"{a[k]} X {b} = {a[k] * b}")
        # yield ('')


my_iter = iter(my_gen(table_shape))
for i in range(2 + len_row * 2):
    for j in range(int(len_row / 2)):
        print(next(my_iter), end="\t\t")
    if i == len_row:
        print('\n\n')
    else:
        print()
