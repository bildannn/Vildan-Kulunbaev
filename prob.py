# class Point3D:
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z
#
#
# point1 = Point3D(1, 2, 3)
# point2 = Point3D(3, 6, 9)
# point3 = Point3D(4, 1, 8)
#
# point1.x = 199
# point1.y = 22
#
# print(f'point1: x = {point1.x}, y = {point1.y}, z = {point1.z}')
# print(f'point2: x = {point2.x}, y = {point2.y}, z = {point2.z}')
# print(f'point3: x = {point3.x}, y = {point3.y}, z = {point3.z}')







# class Box:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#
#     def square(self):
#         print(f'Площадь квадрата равна {self.a} * {self.b} =', self.a * self.b)
#
#
#     def peremeter(self):
#         print(f'Переметр квадрата равна {self.a} + {self.b} + {self.a} + {self.b} = ', (self.a + self.b)*2)
#
#
# s = Box(3, 5)
# s.square()
#
# p = Box(3, 5)
# p.peremeter()








#
# class Triangle:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def squre(self):
#         print(f'Площадь треугольника равна: 0.5 * {self.a} * {self.b} = ', 0.5 * self.a * self.b)
#
#     def peremetr(self):
#         print(f'Периметр треугольника равна =', (((self.a**2) + (self.b**2))**0.5) + self.a + self.b)
#
#
# s = Triangle(3, 5)
# s.squre()
# p = Triangle(3, 5)
# p.peremetr()








# import math
#
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def distance_to(self, other_point):
#         return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)
#
#
# point_a = Point(2, 4)
# point_b = Point(6, 9)
# point_c = Point(6, 0)
#
# distance_ab = point_a.distance_to(point_b)
# distance_bc = point_b.distance_to(point_c)
# distance_ca = point_c.distance_to(point_a)
#
# perimeter = distance_ab + distance_bc + distance_ca
#
# print("Периметр треугольника:", perimeter)








# class CPerson:
#     def __init__(self, name, surname, middle_name, number, month, year, floor):
#         self.name = name
#         self.surname = surname
#         self.midlle_name = middle_name
#         self.number = number
#         self.month = month
#         self.year = year
#         self.floor = floor
#
#     def info_person(self, name, surname, middle_name, number, month, year, floor):
#         self.name = name
#         self.surname = surname
#         self.midlle_name = middle_name
#         self.number = number
#         self.month = month
#         self.year = year
#         self.floor = floor
#
#     def get_info(self):
#         return f'\n ФИО: {self.name} {self.surname} {self.midlle_name} \n Дата рождения : {self.number}. {self.month}. {self.year} \n Пол: {self.floor}'
#
#
# person = CPerson('Вадим', 'Иванов', 'Ильгизович', 23, 4, 1997, 'Мужской')
# print(person.get_info())
# person.info_person('Азамат', 'Кириев', 'Маратович', 11, 2, 2002, 'M')
# print(person.get_info())





# class Phone:
#     def __init__(self, number, model, weight):
#         self.number = number
#         self.model = model
#         self.weight = weight
#
#     def receiveCall(self, name):
#         print(f'Звонит {name}')
#
#     def getNamber(self):
#         return self.number
#
#
# phone1 = Phone(11322343, 'iphone', 270)
# phone2 = Phone(83345457, 'Redmi', 335)
# phone3 = Phone(555553555, 'Samsung', 230)
# print("Телефон 1:")
# print("Номер:", phone1.number)
# print("Модель:", phone1.model)
# print("Вес:", phone1.weight,'\n')
#
# print("Телефон 2:")
# print("Номер:", phone2.number)
# print("Модель:", phone2.model)
# print("Вес:", phone2.weight,'\n')
#
# print("Телефон 3:")
# print("Номер:", phone3.number)
# print("Модель:", phone3.model)
# print("Вес:", phone3.weight,'\n')
#
# phone1.receiveCall('Максим')
# print('Номер телефона:', phone1.number)
# phone2.receiveCall('Раиль')
# print('Номер телефона:', phone2.number)
# phone3.receiveCall('Данил')
# print('Номер телефона:', phone3.number)







# class Reader:
#     def __init__(self, full_name, ticket, faculty, num, month, year, number):
#         self.full_name = full_name
#         self.tiket = ticket
#         self.faculty = faculty
#         self.num = num
#         self.month = month
#         self.year = year
#         self.number = number
#
#     def takeBook(self, num_books):
#         print(f'{self.full_name} взял {num_books} книги')
#
#
#     def returnBook(self, num_books):
#         print(f'{self.full_name} вернул {num_books}')
#
# reader = Reader('Петр Гринев Алексеевич', 5243653, 'Факультет информатики', 22, 5, 2002, 7937676756434)
# reader.takeBook(4)
# reader.returnBook(2)