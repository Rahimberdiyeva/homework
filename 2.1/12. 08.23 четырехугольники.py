import json
import itertools
# from triangle import Triangle
from math import sqrt

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Quadrilateral:
    def __init__(self, p1, p2, p3, p4):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4
# формула Гаусса для многоугольников
    def area(self):
        return abs(0.5 * (self.p1[0] * (self.p2[1] - self.p4[1]) + self.p2[0] * (self.p3[1] - self.p1[1]) + self.p3[0] * (self.p4[1] - self.p2[1]) + self.p4[0] * (self.p1[1] - self.p3[1])))
    # меньше
    def __lt__(self, other):         
        return self.area() < other.area()
    # больше
    def __gt__(self, other):
        return self.area() > other.area()
    # равно
    def __eq__(self, other):
        return self.area() == other.area()
    # меньше или равно 
    def __le__(self, other):
        return self.area() <= other.area()
    # больше или равно
    def __ge__(self, other):
        return self.area() >= other.area()
    # не равно
    def __ne__(self, other):
        return self.area() != other.area() 
    
with open('точки.txt') as f:
    s = f.readline()
s = s.replace(']','] ')
s = s.replace(', ',',')
s=s.split()
points =[json.loads(s[i]) for i in range(0, len(s)-1, 2)]

quadrilaterals = [Quadrilateral(p1, p2, p3, p4) for p1, p2, p3, p4 in itertools.combinations(points, 4) if Quadrilateral(p1, p2, p3, p4).area() != 0]
   
min_quadrilateral = min(quadrilaterals, key=lambda x: x.area())
max_quadrilateral = max(quadrilaterals, key=lambda x: x.area())

print(f'Минимальная площадь у четырехугольника с координатами {min_quadrilateral.p1},{min_quadrilateral.p2},{min_quadrilateral.p3},{min_quadrilateral.p4} равна {min_quadrilateral.area()}')
print(f'Минимальная площадь у четырехугольника с координатами {max_quadrilateral.p1},{max_quadrilateral.p2},{max_quadrilateral.p3},{max_quadrilateral.p4} равна {max_quadrilateral.area()}')
