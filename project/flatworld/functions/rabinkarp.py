import random
def horner(word,p):
    sum = 0
    for letter in word:
        sum = (sum*128 + ord(letter)) % p
    return sum

def naive_check(word1, word2):
    return word1==word2

def rabinkarp(pattern, sentence):
    splitted = sentence.split('\n')
    p = 89
    changed_list = []
    for _ in pattern:
        changed_list.append(chr(random.randint(33, 127)))
    to_change = "".join(changed_list)
    for i in range(len(splitted)):
        corrected = splitted[i].strip()
        splitted[i]=corrected
    splitted.pop()
    indexes = []
    new_song = ''
    for line in splitted:
        line_added = False
        new_line = ""
        hs = horner(pattern,p)
        for i in range (len(line)-len(pattern)+1):
            if hs == horner(line[i:i+len(pattern)],p):
                if(naive_check(line[i:i+len(pattern)], pattern)):
                    line_added = True
                    indexes.append(i)
                    if not new_line:
                        new_line = line[:i]+to_change+line[i+len(pattern):]
                    else:
                        new_line = new_line[:i]+to_change+line[i+len(pattern):]
        if not line_added:
            new_line = line
        new_song+=new_line+'\n'
    print(new_song)
    print(indexes)
    return indexes, new_song