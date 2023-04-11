
def mochila(w,valores,pesos):

    matriz = [[0 for i in range(w)] for j in range(len(pesos))]

    for i in range(len(matriz)):
        for j in range(w):

            if i == 0:
                matriz[i][j] = 0
            elif i > 0 and pesos[i] > j:
                matriz[i][j] = matriz[i-1][j]
            elif i > 0 and pesos[i] <= j:
                matriz[i][j] = max(matriz[i-1][j],matriz[i][j-pesos[i]]+valores[i])

    return matriz[i][j]

pesos = [3,4,5]
valores = [30,50,60]

print(mochila(8,valores,pesos))

