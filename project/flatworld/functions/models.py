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
        return f"({self.x}, {self.y})"

    __repr__ = __str__

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return False


class inhabitants:
    def __init__(self, id):
        self.id = id
        self.personality = randint(0, 1)
        self.direction = randint(0, 1)

    def __str__(self):
        return f"({self.id}, {self.personality}, {self.direction})"

    __repr__ = __str__

    def to_dict(self):
        return {
            "id": self.id,
            "personality": self.personality,
            "direction": self.direction,
        }
