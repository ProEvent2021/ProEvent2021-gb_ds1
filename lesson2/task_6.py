product = [
    ('компьютер', 20000, 5, 'шт'),
    ('принтер', 6000, 2, 'шт'),
    ('сканер', 2000, 7, 'шт')
]

print("Название товаров", [x[0] for x in product])
print("Цена товаров", [x[1] for x in product])
print("Кол-во товаров", [x[2] for x in product])

numbers = [x[3] for x in product]
def get_unique_numbers(numbers):
    unique = []

    for number in numbers:
        if number in unique:
            continue
        else:
            unique.append(number)
    return unique

print(get_unique_numbers(numbers))