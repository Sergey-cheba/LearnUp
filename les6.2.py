# 2. Разработайте программу, с тремя классами - Rectangle, Triangle, Circle, каждый из которых имеет методы perimeter() 
# (расчет и возврат периметра фигуры) и area() (расчет и возврат площади фигуры). Создать 7 произвольных фигур, 
# сохранить их в списке и циклом выполнить вывод периметра и площади каждого объекта.

class Rectangle():

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def perimeter(self):
        return (self.a + self.b) * 2

    def area(self):
        return self.a * self.b


class Triangle():

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        p = self.perimeter()/2
        return (p*(p-self.a)*(p-self.b)*(p-self.c))**0.5


class Circle():
    def __init__(self, r):
        self.r = r

    def perimeter(self):
        return 2 * 3.14 * self.r

    def area(self):
        return (3.14 * self.r)**2

figures = [Rectangle(4,7), Triangle(3,3,5), Circle(4), Rectangle(7,12), Triangle(7,5,9), Circle(4.4), Rectangle(13,21)]

for figure in figures:
    print("Периметр = " + str(figure.perimeter()))
    print("Площадь = " + str(figure.area()))
