# 2. Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Осуществить вывод данных о пользователе одной строкой.

def list(name, surname, year, city, email, telephone):
    return name, surname, year, city, email, telephone

print(list(name=str(input("Введите имя: ")),
           surname=str(input("Введите фамилию: ")),
           year=int(input("Введите год рождения: ")),
           city=str(input("Введите город: ")),
           email=str(input("Введите email: ")),
           telephone=int(input("Введите телефон: "))))
