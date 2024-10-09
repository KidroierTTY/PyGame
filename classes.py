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

class Airplane:
    def __init__(self):
        self.engines = int(input('Двигатели: '))
        self.seats = int(input('Посадочные места: '))

        print('Самолет собран!')

plane1 = Airplane()
plane2 = Airplane()
plane3 = Airplane()

print(f'Самолет 1: Двигателей: {plane1.engines}, Сидений: {plane1.seats}')
print(f'Самолет 2: Двигателей: {plane2.engines}, Сидений: {plane2.seats}')
print(f'Самолет 3: Двигателей: {plane3.engines}, Сидений: {plane3.seats}')




