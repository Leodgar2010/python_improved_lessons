# ✔ Функция принимает на вход три списка одинаковой длины:
# ✔ имена str,
# ✔ ставка int,
# ✔ премия str с указанием процентов вида «10.25%».
# ✔ Вернуть словарь с именем в качестве ключа и суммой
# премии в качестве значения.
# ✔ Сумма рассчитывается как ставка умноженная на процент премии.
def my_func (names, salary, bonus):
    dic ={}
    for i in range (len(names)):
        dic [names[i]]=salary[i]*(float(bonus[i]))
    return dic
names = ["Вася", "Петя"]
salary = [1000,5000]
bonus = ["10.25","11.20"]
print (my_func(names, salary,bonus))

