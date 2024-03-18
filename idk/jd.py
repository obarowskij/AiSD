from random import randint
class Point:
    def __init__(self,x,y):
        self.x =x
        self.y = y
    

punkty = []
for _ in range(20):
    x = randint(0,10)
    y = randint(0,10)
    punkty.append(Point(x,y))
    
sorted_punkty = sorted(punkty, key=lambda point: (point.y,point.x))

for point in sorted_punkty:
    print(f'({point.x}, {point.y})',end=" ")
print("----------------------------------")
for point in punkty:
    print(f'({point.x}, {point.y})',end=" ")
