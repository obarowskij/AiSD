from collections import deque
from random import randint

class Stack:
    def __init__(self):
        self.items = deque()
    def is_empty(self):
        return len(self.items) == 0
    def push(self, item):
        self.items.append(item)
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __str__(self):
        return f'({self.x}, {self.y})'
    __repr__ = __str__
    
class plaszczaki:
    def __init__(self, x, y, id):
        self.id = id
        #self.x = x
        #self.y = y
        self.personality = randint(0,1)
        self.direction = randint(0,1) #potencjalnie trzeba zrobic z plaszczakow punkty ktore moga miec rece we wszystkie strony swiata
        self.energy = randint(0,100)
        #self.holiday = False
        
    def __str__(self):
        return f'({self.id}, {self.personality}, {self.direction}, {self.energy})' #, , {self.x}, {self.y}, {self.holiday}
    __repr__ = __str__