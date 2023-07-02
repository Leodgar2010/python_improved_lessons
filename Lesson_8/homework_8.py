# Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные
# директории. Результаты обхода сохраните в файлы json, csv и pickle. Для дочерних объектов
# указывайте родительскую директорию. Для каждого объекта укажите файл это или директория. Для
# файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом всех
# вложенных файлов и директорий.
import csv
import os
import json
import pickle


def grab_data(dir_collection):
    dic = {}
    for i in dir_collection:
        if os.path.isdir(i) == True:
            a = os.path.join(os.getcwd(), f'{i}')
            result = {"Это директория": os.path.getsize(a)}
            dic[i] = result
            os.chdir(a)
            dir_col = os.listdir(a)
            grab_data(dir_col)
            os.chdir('../')
        elif os.path.isfile(i)==True:
            a = os.path.join(os.getcwd(), f'{i}')
            result = {"Это файл": os.path.getsize(a)}
            dic[i] = result
    return (dic)


def write_dic_into_csv_json_pickle(dic, filename):
    with (open(f"{filename}.json", 'w', encoding="UTF-8") as fjson,
          open(f"{filename}.csv", 'w', encoding="UTF-8") as fcsv,
          open(f"{filename}.pickle", 'wb') as fpickle):
        json.dump(dic, fjson, ensure_ascii=False, indent=1)
        rows = []
        for k, v in dic.items():
            rows.append({'name': k, 'Value': v})
        csv_write = csv.DictWriter(fcsv, fieldnames=['name', 'Value'])
        csv_write.writeheader()
        csv_write.writerows(rows)
        pickle.dump(dic, fpickle)


dir_collection = os.listdir()
dic = grab_data(dir_collection)
write_dic_into_csv_json_pickle(dic, 'homework_8')
