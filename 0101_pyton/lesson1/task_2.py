import time
seconds = float(input("Введите большое число, а мы рассчитаем сколько это в часах и минутах: "))
time_format = time.strftime("%H:%M:%S", time.gmtime(seconds))
print("Время в часах, минутах и секундах: ", time_format)
