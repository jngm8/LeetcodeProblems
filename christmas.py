temporal = []
arbol = {1:temporal}
nodos = int(input())
lista = []
for i in range(2,nodos+1):
    lista.append(i)
for i in lista:
    palabra = int(input())
    if palabra in arbol:
        temporal.append(i)
    else:
        temporal = []
        arbol[palabra] = temporal
        temporal.append(i)
rta = []
for i in arbol:
    suma = len(arbol[i])
    for j in arbol[i]:
        if j in arbol:
            suma -= 1
    if suma >= 3:
        rta.append("Yes")
    else:
        rta.append("No")
        break

if "No" in rta:
    print("No")
else:
    print("Yes")

