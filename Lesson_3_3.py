def dict_update(data, dic):
    tup = (str, int, float)
    for i in tup:
        lst = []
        for k in data:
            if isinstance(k, i):
                lst.append(k)
        dic[i] = lst


data = ("зима", "весна", "лето", "осень", 1, 2, 3, 4, 1.5, 2.5, 3.5, 4.5)
dic = {}
dict_update(data, dic)
print(dic)

tup = {435, 'greg', 5.6, 'grr', 4, 5, 'rgrg'}
dict_1 = {}
for item in tup:
    # dict_1.setdefault(type(item), []).append(item)
    dict_1[type(item)] = dict_1.get(type(item), []) + [item]

print(dict_1)
