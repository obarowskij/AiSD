def horner(word,p):
    sum = ord(word[0])
    for letter in word[1::]:
        sum = sum*128 + ord(letter)
    return sum%p

pattern = input()
sentence = ['relaksujący podróżuję nauka fantastyczny wygodny nauka', 'nauka dzień miłość nauka', 'tradycyjny piękny nauka planuję kolorowy nauka', 'odpoczywam emocja nauka', 'trenuję oglądam sen studia aktywny nauka']
p = 89
for line in sentence:
    hs = horner(pattern,p)
    for i in range (len(line)-len(pattern)+1):
        if hs == horner(line[i:i+len(pattern)],p):
            print(line[i:i+len(pattern)])