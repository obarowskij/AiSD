import random
from .words import words_list


def generate_song():
    song = []
    words = words_list()
    repeated_word = random.choice(words)

    for _ in range(random.randint(2, 5)):
        vers = []
        for _ in range(5):  
            word = random.choice(words) 
            vers.append(word)
        vers.append(repeated_word)
        vers = " ".join(vers)
        song.append(vers)
        song.append('\n')
    song = " ".join(song)
    return song
