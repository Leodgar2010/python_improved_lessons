# Прочитайте созданный в прошлом задании csv файл без
# использования csv.DictReader.
# Распечатайте его как pickle строку.
import pickle
import csv


def pickle_print(source_file):
    with open(source_file, 'r', encoding='UTF-8') as f1:
        reader = csv.reader(f1)
        print(pickle.dumps(list(reader)))


pickle_print('Lesson_8_6.csv')
