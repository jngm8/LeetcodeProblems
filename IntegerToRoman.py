#Given a number, return its respective number in roman notation
def intToRoman(num: int):
    mapa = {"1":"I",
            "4":"IV",
            "5":"V",
            "9":"IX",
            "10":"X",
            "40":"XL",
            "50":"L",
            "90":"XC",
            "100":"C",
            "400":"CD",
            "500":"D",
            "900":"CM",
            "1000":"M"}
    string = ""
    numero = str(num)
    parejas_lista = list(mapa.items())
    i = 0
    longitud = len(str(num))
    while i < longitud:
        if numero in mapa:
            string += mapa[numero]
            i = longitud
        else:
            if len(numero) == 4:
                multi = int(numero[0])
                for _ in range(multi):
                    string += mapa["1000"]
                numero = numero[1:]
            elif len(numero) == 3:
                if int(numero[0]) <= 3:
                    multi = int(numero[0])
                    for _ in range(multi):
                        string += mapa["100"]
                else:
                    multi = int(numero[0])-int(parejas_lista[10][0][0])
                    if multi == 0:
                        multi +=1
                    if multi > 3: # Caso que sea 9XX
                        string += mapa["900"]
                    if multi < 0: #Caso que sea 4XX
                        string += mapa["400"]
                    if multi > 0 and multi <= 3:
                        if int(numero[0]) == 5:
                            string += mapa["500"]
                        else:
                            string += mapa["500"]
                            for _ in range(multi):
                                string += mapa["100"]
                numero = numero[1:]
            elif len(numero) == 2:
                if int(numero[0]) <= 3:
                    multi = int(numero[0])
                    for _ in range(multi):
                        string += mapa["10"]
                else:
                    multi = int(numero[0])-int(parejas_lista[6][0][0]) # resta por 5 para ver cual caso
                    if multi == 0:
                        multi +=1
                    if multi > 3: # Caso que sea 9XX
                        string += mapa["90"]
                    if multi < 0: #Caso que sea 4XX
                        string += mapa["40"]
                    if multi > 0 and multi <= 3:
                        if int(numero[0]) == 5:
                            string += mapa["50"]
                        else:
                            string += mapa["50"]
                            for _ in range(multi):
                                string += mapa["10"]
                numero = numero[1:]
            elif len(numero) == 1:
                if int(numero[0]) <= 3:
                    multi = int(numero[0])
                    for _ in range(multi):
                        string += mapa["1"]
                else:
                    multi = int(numero[0])-int(parejas_lista[2][0][0])
                    string += mapa["5"]
                    if multi == 0:
                        multi +=1
                    if multi > 3: # Caso que sea 9X
                        string += mapa["9"]
                    if multi < 0: #Caso que sea 4X
                        string += mapa["4"]
                    if multi > 0 and multi <= 3:
                        for _ in range(multi):
                            string += mapa["1"]
            i+=1
    return string

print(intToRoman(58))

#Time:67.19%
#Memory:6.13%