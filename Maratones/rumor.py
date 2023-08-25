cantidades = input().split() #['5','2'] number of characters and number of pair friends

tokenized_gold = input().split() #Gold each character wants

sociales = []
for k in range(int(cantidades[1])):
    tokenized_friends = input().split() #Pair of character that are friends
    sociales.append(tokenized_friends[1])

suma = 0
for i in range(1,int(cantidades[0])+1):
    if str(i) not in sociales:
        suma += int(tokenized_gold[int(i)-1])

print(suma)

            