n = int(input())
for i in range(n):
    x = int(input())
    lista = [100,50,10,5,2,1]
    cuenta = 0
    y=0
    while x != 0:
        if x - lista[y] >= 0:
            cuenta+=1
            x -= lista[y]
            pass
        else:
            y+=1
    print(cuenta)



