from projekt.models.models import plaszczaki
from random import randint
from projekt.functions.Fabryka_generate import factory

inhabitants = []
for i in range(10):
    id = i
    inhabitants.append(plaszczaki(id))