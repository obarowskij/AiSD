from random import randint
class Point:
    def __init__(self,x,y):
        self.x =x
        self.y = y
        self.alfal = 0
        self.alfam = 0
    
    def set_alfa(self,x):
        self.alfam = abs(x) + abs(y)
        if x>=0 and y>=0:
            self.alfal = y
            

punkty = []
for _ in range(20):
    x = randint(-10,10)
    y = randint(-10,10)
    punkty.append(Point(x,y))
    
for point in punkty:
    print(f'({point.x}, {point.y})',end=" ")

obwodka = []
min_y = 20
for point in punkty:
    if point.y < min_y:
        min_y = point.y
with_min_y = []
for point in punkty:
    if point.y == min_y:
        with_min_y.append(point)
min_x = 20
for point in with_min_y:
    if point.x < min_x:
        min_x = point.x

for point in with_min_y:
    if point.x == min_x:
        minimal_point = point
        break
sorted_punkty = []
sorted_punkty.append(minimal_point)
