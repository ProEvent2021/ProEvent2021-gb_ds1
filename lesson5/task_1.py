# 1. Создать программный файл в текстовом формате, записать в него построчно данные, вводимые
# пользователем. Об окончании ввода данных будет свидетельствовать пустая строка.

text_1 = input(str("Введите текст: "))
out_f = open(r'D:\GIT\ProEvent2021-gb_ds1\lesson5\file.txt', 'w')
while True:
    text_1 = input(str("Введите текст: "))
    if text_1 == '': break
    out_f.write(text_1 + '\n')
out_f.close()

out_f = open(r'D:\GIT\ProEvent2021-gb_ds1\lesson5\file.txt', 'r')
for line in out_f:
    print(line)