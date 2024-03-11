def convert(melodia):
    melodia_binarnie = []
    wynik = ""
    for char in melodia:
        if(char!=" "):
            melodia_binarnie.append(bin(ord(char)-97)[2::])
        else:
            melodia_binarnie.append(" ")
    for elem in melodia_binarnie:
        wynik += elem
        wynik += " "
    return wynik
print(convert("boli"))
