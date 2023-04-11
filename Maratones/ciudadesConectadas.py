x = int(input())#Numer de casos

for i in range(x):
    y = int(input)#Numero de elementos en la permutación
    permutas = list(input().split())
    nodos = {}
    lista = []
    for k in permutas:
        lista = []
        for t in permutas:

            if k == t:
                pass
            else:
                if int(k) > int(t):
                    nodos[k] = lista
                    lista.append(t)
                else:
                    break
        print(len(nodos))