import random
from .words import words_list


def generate_song():
    song = ""
    words = words_list()
    for _ in range(
        random.randint(2, 5)
    ):  # Random number of verses between 2 and 5
        vers = ""
        for _ in range(
            random.randint(3, 6)
        ):  # Random number of words in each verse between 3 and 6
            word = random.choice(words)  # Get a random word from the list
            vers += word + " "  # Add the word to the verse
        song += (
            vers.strip().capitalize() + "\nbr\n"
        )  # Add the verse to the song, followed by a newline character and "br"
    return song
