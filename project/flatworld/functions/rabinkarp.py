def horner(word,p):
    sum = 0
    for letter in word:
        sum = (sum*128 + ord(letter)) % p
    return sum

def rabinkarp(pattern, sentence):
    print(pattern)
    print(sentence)
    p = 89

    hs = horner(pattern,p)
    for i in range (len(sentence)-len(pattern)+1):
        if hs == horner(sentence[i:i+len(pattern)],p):
            print(sentence[i:i+len(pattern)])