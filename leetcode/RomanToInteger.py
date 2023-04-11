#Given a number in roman notation, return it in decimal notation
def romanToInt(s: str):
    mapa = {"I":"1",
            "IV":"4",
            "V":"5",
            "IX":"9",
            "X":"10",
            "XL":"40",
            "L":"50",
            "XC":"90",
            "C":"100",
            "CD":"400",
            "D":"500",
            "CM":"900",
            "M":"1000"}#Se hace un mapa con todas las posibles combinaciones de numeros distintos
    suma = 0
    i = 0
    while i < len(s):
        try:# Se usa cuando estoy en la ultima letra y lanza excepcion porque se sale de los limites 
            pareja = s[i] + s[i+1]#Saco un par de letras  
            if s[i] in mapa and pareja not in mapa:#Reviso si la letra actual esta en el mapa
                suma += int(mapa[s[i]])#Suma lo correspondiente a la letra en el mapa
            else: # Si primero si esta en el mapa 
                suma += int(mapa[pareja])
                i+=1
        except:
            pareja = s[i-1]+s[i]#Si lanza error por estar en la ultima posicion, forma la pareja con el ultimo y penultimo
            if s[i] in mapa and pareja not in mapa:
                suma += int(mapa[s[i]])
            else:
                suma += int(mapa[pareja])
                i+=1
        i+=1
    return suma

print(romanToInt("MCMXCIV"))

#Time:74.19%
#Memory:30.7%