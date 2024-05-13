def horner(word,p):
    sum = ord(word[0])
    for letter in word[1::]:
        sum = sum*128 + ord(letter)
    return sum%p

