import random
from .words import words_list


def generate_song():
    song = ""
    words = words_list()
    repeated_word = random.choice(words)

    for _ in range(random.randint(2, 5)):
        vers = ""
        for _ in range(random.randint(2, 5)):  
            word = random.choice(words) 
            vers += word + " " 
        vers += repeated_word + " " 
        song += (vers.strip().capitalize() + "\nbr\n")
    return song
