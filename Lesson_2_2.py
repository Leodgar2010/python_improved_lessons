data = [23, "лето", 3.14, True]
for i,k in enumerate (data):
    print (i,k)
for k,i in enumerate (data):
    print(f"Порядковый номер: {k + 1}\n\
           Значение: {i}\n\
           Адрес в памяти: {id(i)}\n\
           Размер в памяти: {i.__sizeof__()}\n\
           Хэш: {hash(i)}")
    if (type(i) == int):
        print (f"\t\t   Это целое число {i}")
    elif (isinstance(i,str)):
        print (f"\t\t   Это строка {i}")
    else:
        pass
