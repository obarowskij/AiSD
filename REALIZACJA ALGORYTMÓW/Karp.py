def horner(word,p):
    sum = ord(word[0])
    for letter in word[1::]:
        sum = sum*128 + ord(letter)
    return sum%p

pattern = input()
sentence = input()
p = 89

hs = horner(pattern,p)
for i in range (len(sentence)-len(pattern)+1):
    if hs == horner(sentence[i:i+len(pattern)],p):
        print(i)
