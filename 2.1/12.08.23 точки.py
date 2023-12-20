import json
import itertools

class Triangle:
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.area = 0.5 * abs(self.p1[0] * (self.p2[1] - self.p3[1]) + self.p2[0] * (self.p3[1] - self.p1[1]) + self.p3[0] * (self.p1[1] - self.p2[1]))
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

points = [json.loads(s[i]) for i in range(0, len(s))]
   
triangles = [Triangle(p1, p2, p3) for p1, p2, p3 in itertools.combinations(points, 3) if Triangle(p1, p2, p3).area!=0]

min_triangle, max_triangle = min(triangles), max(triangles)

print(f'Минимальная площадь у треугольника с координатами {min_triangle.p1},{min_triangle.p2},{min_triangle.p3} равна {min_triangle.area}')
print(f'Минимальная площадь у треугольника с координатами {max_triangle.p1},{max_triangle.p2},{min_triangle.p3} равна {max_triangle.area}')
