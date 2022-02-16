# 2. Создать текстовый файл (не программно), сохранить в нём несколько строк,
# выполнить подсчёт строк и слов в каждой строке.

with open("file2.txt") as f_obj:
    lines = 0
    for line in f_obj:
        lines += 1
        result = len(line.split())

    print(f"{lines} строк в файле")
    print(f"Количество слов в файле - {result}")
