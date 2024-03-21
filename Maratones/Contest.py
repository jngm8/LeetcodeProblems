import math as m

tupla = [int(i) for i in input().split()]

lista = []
for i in range(tupla[0]):
    lista.append(int(input()))
lista.sort()

numerador = (m.factorial(tupla[0]))
denominador = (m.factorial(tupla[1]))*(m.factorial(tupla[0]-tupla[1]))
combinacion = int(numerador/denominador)

print(combinacion)

final = []
t = [0 for _ in range(tupla[1])]
for i in range(len(lista)):
    for j in range(0,len(lista)):
        combinaciones = []
        combinaciones.append(lista[i])
        combinaciones.append(lista[j])
        try:
            for u in range(j+1,j+int(tupla[1])-1): # desde j+1 porque j ya lo inclui la pos de j + los numeros que quiero incluir
                combinaciones.append(lista[u])
        except:
            combinaciones = []
            break

        final.append(combinaciones)
print(len(final))
rta = 0
for comb in final:
    for num in range(2,len(comb)):

        if comb[num-2] + comb[num-1] >= comb[num]:
            if num == len(comb)-1:
                rta += 1
        else:
            break
print(rta)