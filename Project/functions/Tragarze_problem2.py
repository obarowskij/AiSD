from projekt.models.models import plaszczaki
from random import randint
import math
from projekt.functions.plaszczki_generate import inhabitants
from projekt.functions.Fabryka_generate import factory
from projekt.functions.Graham_problem1 import hull_points

def calculate_distance(point1, point2):
    return math.sqrt((point1.x - point2.x)**2 + (point1.y - point2.y)**2)

matching_personality_direction = {}
matching_personality_direction[0] = {0: [], 1: []}
matching_personality_direction[1] = {0: [], 1: []}
bearers = []
for person in inhabitants:
    matching_personality_direction[person.personality][person.direction].append(person)

for j in range(2):
    while matching_personality_direction[j][0] and matching_personality_direction[j][1]:
        bearers.append((matching_personality_direction[j][0].pop(), matching_personality_direction[j][1].pop()))

for pair in bearers:
    print(pair)
    print()
    
total_distance = 0
for i in range(len(hull_points) - 1):
    distance = calculate_distance(hull_points[i], hull_points[i+1])
    total_distance += distance

total_distance += calculate_distance(hull_points[-1], hull_points[0])
total_distance = round(total_distance, 2)
print(f'total distance: {total_distance}')

total_time = 0
factory_point = hull_points[0]

for i in range(len(hull_points)):
    distance_to_point = calculate_distance(factory_point, hull_points[i])
    total_time += distance_to_point
    if i < len(hull_points) - 1:
        distance_to_next_point = calculate_distance(hull_points[i], hull_points[i+1])
        total_time += distance_to_next_point

total_time += calculate_distance(hull_points[-1], factory_point)

print(f'total time: {total_time} seconds')