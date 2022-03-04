# 6. Реализовать два небольших скрипта:
# итератор, генерирующий целые числа, начиная с указанного;
# итератор, повторяющий элементы некоторого списка, определённого заранее.
# Подсказка: используйте функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным.
# Предусмотрите условие его завершения. #### Например, в первом задании выводим целые числа, начиная с 3.
# При достижении числа 10 — завершаем цикл. Вторым пунктом необходимо предусмотреть условие,
# при котором повторение элементов списка прекратится.

from itertools import count
from itertools import cycle


def count_func(start_number, stop_number):
    for el in count(start_number):
        if el > stop_number:
            break
        else:
            print(el)


def cycle_func(list, iteration):
    i = 0
    iter = cycle(list)
    while i < iteration:
        print(next(iter))
        i += 1


count_func(start_number=3, stop_number=10)
cycle_func(list=[1, 2], iteration=5)
