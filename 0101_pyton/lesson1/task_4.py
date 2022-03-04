number = int(input("Введите любое целое число:"))
ls = []
while number > 10:
    ls.append(number % 10)
    number //= 10
number_2 = max(ls)
print(number_2)
