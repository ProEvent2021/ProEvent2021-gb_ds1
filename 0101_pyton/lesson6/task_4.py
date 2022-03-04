# 4. Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А также методы: go,
# stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60
# (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
# выведите результат. Вызовите методы и покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} поехала вперед'

    def stop(self):
        return f'{self.name} остановилась'

    def turn_right(self):
        return f'{self.name} сделала поворот направо'

    def turn_left(self):
        return f'{self.name} сделала поворот налево'

    def show_speed(self):
        return f'Скорость машины {self.name}  {self.speed} км.ч.'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Скорость машины {self.name} {self.speed} км.ч.')

        if self.speed > 40:
            return f'Машина {self.name} превышает скорость в городе'
        else:
            return f'Машина {self.name} соблюдает скоростной режим'

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Скорость рабочей машины {self.name} {self.speed} км.ч.')

        if self.speed > 60:
            return f'Машина {self.name} нарушает скоростной режим'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} получает штраф от ГАИ'
        else:
            return f'{self.name} не получает штраф от ГАИ'


audi = SportCar(90, 'Желтая', 'Ауди', False)
oka = TownCar(20, 'Черная', 'Ока', False)
lada = WorkCar(80, 'Белая', 'Лада', True)
ford = PoliceCar(60, 'Синий',  'Форд', True)
print(lada.turn_left())
print(f'Когда {oka.turn_right()}, то {audi.stop()}')
print(f'{lada.go()} , когда скорость будет выше положенной {lada.show_speed()}')
print(f'{lada.name} {lada.color}')
print(audi.show_speed())
print(oka.show_speed())
print(ford.police())
print(ford.show_speed())
