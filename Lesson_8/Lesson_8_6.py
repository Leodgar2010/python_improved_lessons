# Напишите функцию, которая преобразует pickle файл
# хранящий список словарей в табличный csv файл.
# Для тестированию возьмите pickle версию файла из задачи
# 4 этого семинара.
# Функция должна извлекать ключи словаря для заголовков
# столбца из переданного файла.
import csv
import pickle


def pickle_to_csv(source_file, result_file):
    with (open(source_file, 'rb') as f1,
          open(result_file, 'w', encoding='UTF-8') as f2):
        lst = pickle.load(f1)
        print(lst)
        csv_write = csv.DictWriter(f2, fieldnames=['id', 'level', 'name', 'hash'])
        csv_write.writeheader()
        csv_write.writerows(lst)


pickle_to_csv('Lesson_8_4.pickle', 'Lesson_8_6.csv')
