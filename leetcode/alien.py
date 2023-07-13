def alienAlfabeto(palabras,alfabeto):
    mapa = {}
    #Agregamos la llave y el valor al hash map
    for i in range(len(alfabeto)):
        mapa[alfabeto[i]] = i
    apuntadorPalabra = 0
    while apuntadorPalabra < len(palabras)-1:
        centinela = True
        apuntadorLetra = 0
        while apuntadorLetra < len(palabras[apuntadorPalabra]) and centinela:
            #Comparamos letra por letra
            if apuntadorLetra < len(palabras[apuntadorPalabra]) and apuntadorLetra < len(palabras[apuntadorPalabra+1]):
                if (mapa.get(palabras[apuntadorPalabra][apuntadorLetra])-mapa.get(palabras[apuntadorPalabra+1][apuntadorLetra]))<=0:
                    #Si cumple la regla del diccionario pero son distintas letras, no compare el siguiente par
                    if palabras[apuntadorPalabra][apuntadorLetra] != palabras[apuntadorPalabra+1][apuntadorLetra]:
                        centinela = False
                        apuntadorPalabra+=1
                    apuntadorLetra += 1
                else:
                    return False
            else:
                #Si la longitud de la palabra anterior es mayor que la que le sigue, entonces ya sabemos que el diccionario esta desorganizado
                if len(palabras[apuntadorPalabra]) > len(palabras[apuntadorPalabra+1]):
                    return False
                apuntadorPalabra+=1
                centinela = False
        if apuntadorLetra == len(palabras[apuntadorPalabra]):
            apuntadorPalabra+=1
    return True
        

print(alienAlfabeto(["conocer","cono"],"abcdefghijklmnopqrstuvwxyz"))

print(alienAlfabeto(["habito","hacer","lectura","sonreir"],"hlabcdefgijkmopqrstuvwxyz"))

print(alienAlfabeto(["hello","hello"],"abcdefghijklmnopqrstuvwxyz"))

print(alienAlfabeto(["zezwvpdhkhc","nldmzkh","qvjpbis","gxntgh","knkdjzzxkv","qyymcxdjut","htjghmlc","qxgxzmgbodnj","hkmhfenu","tlbjlaw"],"pojvhubakxzqtlesmcwydinrfg"))

print(alienAlfabeto(["app","apple"],"abcdefghijklmnopqrstuvwxyz"))
