import json
import itertools

class Triangle:
    def __init__(self, p1, p2, p3):
        self.a = p1
        self.b = p2
        self.c = p3
        self.area = 0.5 * abs(self.a[0] * (self.b[1] - self.c[1]) + self.b[0] * (self.c[1] - self.a[1]) + self.c[0] * (self.a[1] - self.b[1]))
    # меньше
    def __lt__(self, other):         
        return self.area < other.area
    # больше
    def __gt__(self, other):
        return self.area > other.area
    # равно
    def __eq__(self, other):
        return self.area == other.area
    # меньше или равно 
    def __le__(self, other):
        return self.area <= other.area
    # больше или равно
    def __ge__(self, other):
        return self.area >= other.area
    # не равно
    def __ne__(self, other):
        return self.area != other.area 
    

with open('точки.txt') as f:
    s = f.readline()
s = s.replace(']','] ')
s = s.replace(', ',',')
s=s.split()
points =[json.loads(s[i]) for i in range(0, len(s))]
   
triangles = [Triangle(p1, p2, p3) for p1, p2, p3 in itertools.combinations(points, 3) if Triangle(p1, p2, p3).area!=0]

min_triangle, max_triangle = min(triangles), max(triangles)

print(f'Минимальная площадь у треугольника с координатами {min_triangle.a},{min_triangle.b},{min_triangle.c} равна {min_triangle.area}')
print(f'Минимальная площадь у треугольника с координатами {max_triangle.a},{max_triangle.b},{max_triangle.c} равна {max_triangle.area}')
