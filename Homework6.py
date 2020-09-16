# Задание 1

'''
Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный.
В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном порядке
(красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить
соответствующее сообщение и завершать скрипт.
'''

from time import sleep


class TrafficLight:

    def __init__(self):
        self.__color = ['красный', 'желтый', 'зеленый']

    def running(self, ):
        i = 0
        while i < len(self.__color):
            print(f'Горит {self.__color[i]} cвет')
            if i == 0:
                sleep(7)
            elif i == 1:
                sleep(2)
            elif i == 2:
                sleep(5)
            i += 1


a = TrafficLight()
a.running()

# Задание 2

'''
Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина). 
Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными. 
Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна. 
Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом, 
толщиной в 1 см * чи сло см толщины полотна. Проверить работу метода.
Например: 20м * 5000м * 25кг * 5см = 12500 т
'''


class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width
        self._mass = 25
        self._thickness = 0.05

    def road_mass(self):
        print(
            f'Масса асфальта = {self._length}*{self._width}*{self._mass}*{self._thickness} = '
            f'{self._length * self._width * self._mass * self._thickness}т')


b = Road(5000, 20)
b.road_mass()

# Задание 3

'''
Реализовать базовый класс Worker (работник), 
в котором определить атрибуты: name, surname, position (должность), income (доход). 
Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например, 
{"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker. 
В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и 
дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных 
(создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).
'''


class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):
    def get_full_name(self):
        print(f'Имя и фамилия: {self.name} {self.surname}')

    def get_total_income(self):
        total_income = 0
        for key, val in self._income.items():
            total_income = total_income + val
        print(f'Доход с учетом премии: {total_income}')


a = Position('Петя', 'Иванова', 'Президент', {"wage": 1000, "bonus": 500})
a.get_full_name()
a.get_total_income()
print(f'Имя: {a.name} \nФамилия: {a.surname} \nДолжность: {a.position}')

# Задание 4

'''
Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево). 
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда). 
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. 
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля. 
Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) 
должно выводиться сообщение о превышении скорости.
'''


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'Машина поехала')

    def stop(self):
        print(f'Машина остановилась')

    def turn(self, direction):
        print(f'Машина повернула на {direction}')

    def show_speed(self):
        print(f'Текущая скорость автомобиля: {self.speed}')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'Вы превысили ограничение скорости 60км/ч. Ваша скорость = {self.speed}')


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'Вы превысили ограничение скорости 40км/ч. Ваша скорость = {self.speed}')


class SportCar(Car):
    def acceler(self, accel_speed):
        print(f'Разгон до 100 км/ч за {accel_speed}')


class PoliceCar(Car):
    def flasher(self, flasher_on):
        if flasher_on:
            print(f'Включена мигалка')
        else:
            print(f'Мигалка выключена')


a = PoliceCar(120, 'белая', 'Приора', True)
a.go()
a.turn('право')
a.flasher(True)
a.show_speed()
a.stop()
print(a.name)

b = WorkCar(50, 'Красный', 'Камаз', False)
b.show_speed()

# Задание 5

'''
Реализовать класс Stationery (канцелярская принадлежность). 
Определить в нем атрибут title (название) и метод draw (отрисовка). 
Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw. 
Для каждого из классов методы должен выводить уникальное сообщение. 
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
'''


class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print(f'{self.title} для записи в тетради')


class Pencil(Stationery):
    def draw(self):
        print(f'{self.title} для эскизов')


class Handle(Stationery):
    def draw(self):
        print(f'{self.title} для выделения текста')


a = Pen('Ручка')
print(f'Это {a.title}')
a.draw()

b = Pencil('Карандаш')
print(f'Это {a.title}')
b.draw()

c = Handle('Маркер')
print(f'Это {a.title}')
c.draw()
