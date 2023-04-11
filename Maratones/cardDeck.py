casos = list(input().split())

cartas = list(input().split())

queries = list(input().split())

for i in range(len(queries)):
    for j in range(len(cartas)):
        if cartas[j] == queries[i]:
            cartas.insert(0,cartas[j])
            cartas.pop(j+1)
            print(j+1)
            break


