

coordenadas = {(0,0):[(0,80),(40,0)],
               (0,80):[(0,0),(20,60)],
               (20,60):[(0,80),(40,20)],
               (40,20):[(20,60),(40,0)],
               (40,0):[(40,20),(0,0)]}


lista_fevs = list(coordenadas.keys())

x = lista_fevs[0][0]

y = lista_fevs[0][1]

ecuacion = 3*x + 3*y

maximo = ecuacion

longitud = len(coordenadas)

conteo = 0

centi = True

posicion = 0

while conteo < longitud and centi:

    parado = len(coordenadas[(x,y)])

    nuevoConteo = 0

    dicci =  {}

    mayorActual = 3*lista_fevs[posicion][0] + 2*lista_fevs[posicion][1]

    dicci[(x,y)] = mayorActual

    while nuevoConteo < parado:

        operacion = 3*coordenadas[(x,y)][nuevoConteo][0] + 2*coordenadas[(x,y)][nuevoConteo][1]

        dicci[(coordenadas[(x,y)][nuevoConteo][0],coordenadas[(x,y)][nuevoConteo][1])] = operacion

        nuevoConteo +=1

    f=0
    for i in dicci:
        if dicci[i] > mayorActual:
            mayorActual = dicci[i]
            llave = i
            f+=1

    max_valor = dicci[llave]

    posicion = lista_fevs.index(llave)

    x = lista_fevs[posicion][0]
    y = lista_fevs[posicion][1]

    conteo +=1

    if f == 0:
        
        centi = False

    dicci.clear()

    


    










