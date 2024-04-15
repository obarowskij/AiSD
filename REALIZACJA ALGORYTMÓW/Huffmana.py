text = input()
length = len(text)
frequency = {}
for elem in text:
    if elem not in frequency.keys():
        frequency.update({elem:text.count(elem)/length})
frequency = dict(sorted(frequency.items(), key=lambda x:x[1],reverse=True))
print(frequency)
code = {}
count = ''
for elem in frequency.keys():
    if elem == list(frequency.keys())[-1]:
        code.update({elem:count})
    else:
        temp = f'{count}0'
        code.update({elem:temp})
        count = f'1{count}'
print(code)
coded_text = ''
for letter in text:
    coded_text = f'{coded_text}{code[letter]}'

print(coded_text)
