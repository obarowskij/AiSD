# n - liczba wierzcholkow
# m - liczba krawedzi
print("podaj liczbe wierzcholkow i krawedzi:")
n,m = map(int,input().split())
print("graf(1) czy digraf(2):")
match int(input()):
    #---------------------------------------------------------------#
    case 1:
        lista_sasiadow = [[] for _ in range(n)]
        macierz = [[0] * (n) for _ in range(n)]
        for i in range(m):
            l = list(map(int,input().split()))
            if len(l) == 2:
                l.append(0)
            lista_sasiadow[l[0]].append((l[1],l[2]))
            lista_sasiadow[l[1]].append((l[0],l[2]))
            macierz[l[0]][l[1]] = l[2]
            macierz[l[1]][l[0]] = l[2]
        print("lista sasiadow: ", lista_sasiadow)
        print("macierz sasiadow: ", macierz)
        
        liczba_krawedzi = [0]
        indeks = 0
        for elem in lista_sasiadow:
            pass

    #---------------------------------------------------------------#
    case 2:
        macierz = [[0] * (n) for _ in range(n)]
        lista_sasiadow = [[] for _ in range(n)]  
        for i in range(m):
            l = list(map(int,input().split()))
            if len(l) == 2:
                l.append(0)
            macierz[l[0]][l[1]] = l[2]
            lista_sasiadow[l[0]].append((l[1],l[2]))
        print("lista sasiadow: ", lista_sasiadow)
        print("macierz sasiadow: ", macierz)
        
        tablica = [0 for _ in range(n + 1)]
        tablica[n] = m
        tablica_somsiad = [[0,0] for _ in range(m)]
        k = 0
        for i in range(n):
            length = len(lista_sasiadow[i]) + tablica[i]
            tablica[i+1] = length
            for j in range(len(lista_sasiadow[i])): 
                tablica_somsiad[k][0] = lista_sasiadow[i][j][0]
                tablica_somsiad[k][1]= lista_sasiadow[i][j][1]
                k += 1
        print("tablica indeksow: ", tablica)
        print("tablica sąsiadow: ", tablica_somsiad)
    #---------------------------------------------------------------#
    case _:
        print("nie ma takiego przypadku")
        


"""graf
4 4
1
0 3 4
0 2 2
2 3 6
1 3 5
"""

"""digraf
4 5
2
0 1 4
0 2 3
1 3 2
3 1 1
3 2 6
"""
