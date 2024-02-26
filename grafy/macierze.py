n = int(input())
m = int(input())
lista_sasiadow = []
lista_sasiadow_s = []
macierz = []
macierz_s = []

for _ in range(n):
    lista_sasiadow.append([])

for i in range(n):
    macierz.append([])
    for j in range(n):
        macierz[i].append(0)

for i in range(m):
    l = list(map(int,input().split()))
    if len(l) == 2:
        l.append(0)
    lista_sasiadow[l[0]].append((l[1],l[2]))
    lista_sasiadow[l[1]].append((l[0],l[2]))
    macierz[l[0]][l[1]] = l[2]
    macierz[l[1]][l[0]] = l[2]
    macierz_s[l[0]][l[1]] = l[2]
    lista_sasiadow_s[l[0]].append((l[1],l[2]))
#graf
    
#dgraf