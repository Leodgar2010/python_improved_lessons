from random import randint, uniform


def write_file(filename, row_count):
    with open(filename, 'a', encoding='utf-8') as f:
        for _ in range(row_count):
            a, b = randint(-1000, 1000), uniform(-1000, 1000)
            f.write(f"{a}|{b}")


write_file('numbers.txt', 5)
