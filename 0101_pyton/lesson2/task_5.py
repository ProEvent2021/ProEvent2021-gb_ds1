rating = int(input("Введите число: "))
my_list = [7, 5, 3, 3, 2]
c = my_list.count(rating)
for key in my_list:
    if c > 0:
        i = my_list.index(rating)
        my_list.insert(i + c, rating)
        break
    else:
        if rating > key:
            j = my_list.index(key)
            my_list.insert(j, rating)
            break
        elif rating < my_list[len(my_list) - 1]:
            my_list.append(rating)
print(my_list)
