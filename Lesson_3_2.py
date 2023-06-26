def has_uppercase_letter(string):
    for char in string:
        if char.isupper():
            return True
    return False

data = (input("Введите строку: "))

if data.isdecimal() and int(data)>0:
    data=int(data)
elif data.count(".")==1 and len(data.split("."))>1 and data.replace('.','').isdecimal():
    data=float(data)
elif has_uppercase_letter(data):
    data = data.lower()
else:
    data = data.upper()
print (f"Тип данных: {type(data)} Значение: {data}")
