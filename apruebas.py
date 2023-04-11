permutas = [3,2,1,6,5,4]
nodos = {}
x = 0
y = 1
lista = []
while nodos:
    if permutas[x] > permutas[y]:
        nodos[permutas[x]] = lista
        lista.append(permutas[y])
        
    else:
        lista = []
        nodos[permutas[x]] = lista
print(len(nodos))

