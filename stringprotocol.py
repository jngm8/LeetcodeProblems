caso = int(input())
for i in range(caso):
    lon = int(input())
    suma = 0
    palabra = input()
    j = 0
    while j < len(palabra):
        try:
            if palabra[j] == palabra[j+1]:
                suma +=1
                j += 2
            else:
                j+=1
                suma+=1
        except:
                suma+=1
                j+=1
    print(suma)


    
 


