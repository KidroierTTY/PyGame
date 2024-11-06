#class Class_name:
#   ...

# class Car:
#     wheels = 4
#     engine = 1
#     color = 'white'
#
#
# print(Car)
# moskvich = Car()
# volga = Car()
# niva = Car()
#
# print(Car.color)
# print(moskvich.color)
# print(volga.color)
# print(niva.color)
#
# moskvich.color = 'red'
# volga.color = 'violet'
# niva.color = 'pon'
#
# print(moskvich.color)
# print(volga.color)
# print(niva.engine)

# class Airplane:
#     engines = ...
#     seats = ...
#
# Airplane.engines = input('Двигатели: ')
# Airplane.seats = input('Сидения: ')
#
# print(Airplane.engines)
# print(Airplane.seats)

# import qrcode
#
# data = 'Hello, world!'
#
# # img = qrcode.make(data)
#
# qr = qrcode.QRCode(version=5, box_size=15, border=10)
#
# qr.add_data(data)
#
# img = qr.make_image()
#
# img.save('test.png')

# KONSTRUCTOR CLASSOV

# class Airplane:
#     def __init__(self):
#         self.engines = int(input('Двигатели: '))
#         self.seats = int(input('Посадочные места: '))
#
#         print('Самолет собран!')
#
# plane1 = Airplane()
# plane2 = Airplane()
# plane3 = Airplane()
#
# print(f'Самолет 1: Двигателей: {plane1.engines}, Сидений: {plane1.seats}.')
# print(f'Самолет 2: Двигателей: {plane2.engines}, Сидений: {plane2.seats}.')
# print(f'Самолет 3: Двигателей: {plane3.engines}, Сидений: {plane3.seats}.')

# class Car:
#     def __init__(self):
#         self.color = str(input("Цвет: "))
#         self.brand = str(input("Бренд: "))
#         self.speed = int(input("Максимальная скорость: "))
#
#         print("Автомобиль готов!")
#
# Car1 = Car()
#
# print(f"Машина 1: Бренд: {Car1.brand}, Цвет: {Car1.color}, Максимальная скорость: {Car1.speed}")

# class Animal:
#     def __init__(self, name):
#         self.name = name
#
#     def bring_destruction(self):
#         print(f'{self.name} что-то сломал!')
#
#
# class Dog(Animal):
#     def __init__(self, name):
#         Animal.__init__(self, name)
#
#     def make_sueta(self):
#         print(f'{self.name} играет с диваном')
#
#
# class Cat(Animal):
#     def __init__(self, name):
#         Animal.__init__(self, name)
#
#     def make_sueta(self):
#         print(f'{self.name} тыгыдыкает в 5 утра по лицу')
#
#
# dog = Dog('Барбос')
# cat = Cat('Елкалаз')


# class Kettle:
#     def turn_on(self):
#         print('Чайник включился')
#         self.__boil()
#         self.__check_t()
#         self.__beep()
#         self.__turn_off()
#     def __boil(self):
#         print('Вода греется, пузырьки мутятся')
#     def __check_t(self):
#         print('Проверяется температура')
#     def __beep(self):
#         print('Вода нагрелась, издает звук')
#     def __turn_off(self):
#         print('Чайник выключился')
# # Создаем объект чайника
# chaynik = Kettle()
# # Включаем его
# chaynik.turn_on()

# chaynik.__check_t()
# chaynik.__boil()

# Допиши код везде, где стоит "..."
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

#     def set_balance(self, balance):
#         self.__balance = balance
#
#     def get_balance(self):
#         print(f"Баланс: {self.__balance}")
#
#     def add(self):
#         balance_do = self.__balance
#         self.value = int(input("Сколько денег хотите начислить: "))
#         self.__balance += self.value
#         print(f"Деньги пополнены! Было денег: {balance_do}, Стало денег: {self.__balance}")
#
#     def remove(self):
#         balance_do = self.__balance
#         self.value = int(input("Сколько денег хотите снять: "))
#
#         if self.value > self.__balance:
#             print("Ошибка: на счете недостаточно средств")
#         else:
#             self.__balance -= self.value
#             print(f"Деньги снялись! Было денег: {balance_do}, Стало денег: {self.__balance}")
#
# visa = BankAccount(1000)
#
# visa.remove()
# visa.get_balance()
# visa.add()
# visa.get_balance()
