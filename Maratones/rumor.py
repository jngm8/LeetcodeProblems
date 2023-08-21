quantities = input() # number of characters and number of pair friends
quantities += " "
def resolucion(quantities):
    lista = [] 
    string = ""
    for i in quantities:
        if i != " ":
            string += i
        else:
            lista.append(string)
            string = ""

    return lista #Lista tokenizada

gold = input()
gold += " "
gold = resolucion(gold)
lista = resolucion(quantities) # ['5','2'] number of characters and number of pair friends

adyacencias = {}
for i in range(1,int(lista[0])+1):
    adyacencias[i] = []

array_friends = []

for k in range(int(lista[1])):
    friends = input()# Pair of character that are friends
    friends += " "
    array_friends.append(resolucion(friends)) #[['1', '4'], ['4', '5']]

#Devuelve una lista de adyacencias indicandome el individuo y todos sus amigos
for i in range(1,int(lista[0])): # Complejidad n*m, pues por cada individuo(n) reviso todos los amigos(m)
    for j in range(int(len(array_friends))):
        if int(array_friends[j][0]) == i: # Si hay un character que tiene amigos
            adyacencias[i].append(array_friends[j][1])
            #adyacencias[int(array_friends[j][1])].append(array_friends[j][0])

# Agrego lod amigos que son amigos de los que cotactan. La rosca
sociales = []
for amigo in adyacencias:
    for cariñosos in adyacencias[amigo]:
        sociales.append(cariñosos)

print(sociales)
print(gold)

suma = 0


            