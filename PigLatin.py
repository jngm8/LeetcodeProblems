"""
El Pig Latin es un lenguaje construido a partir de la transformación de palabras en inglés. 
Aunque se desconoce el origen de dicho lenguaje, este es mencionado en al menos dos documentos 
del siglo XIX, lo cual sugiere que ha existido por más de cien años.

Las siguientes son las reglas que se usan para traducir del inglés al Pig Latin:

Si una palabra empieza por una consonante, todas las letras del inicio de la palabra, hasta la 
primera vocal, se eliminan y luego se agregan al final de la palabra, seguidas de “ay”. Por ejemplo, 
“computer” se traduce a “omputercay” y “think” se traduce a “inkthay”.
Si una palabra inicia por vocal, se agrega “way” al final de la palabra. Por ejemplo, “algorithm” 
se traduce a “algorithmway” y “office” se convierte en “officeway”.
Si una palabra no tiene vocales (por ejemplo "my"), entonces no se cambia de ninguna forma.
Cree una función que reciba como parámetro un texto (conformado por una o más palabras), y retorne
 la traducción de dicho texto a Pig Latin. Puede asumir que el texto ingresado por el usuario consiste
  solamente de palabras en minúscula y separadas por espacios.
"""


def traducir_a_pig_latin(texto: str)->str:

    lista = texto.split()

    i = 0

    while i < len(lista):

      if lista[i][0] == "a" or lista[i][0] == "e" or lista[i][0] == "i" or lista[i][0] == "o" or lista[i][0] == "u":

        lista[i] = lista[i][:len(lista[i])] + "way"

      else:

        j = 0

        while j < len(lista[i]):

          if lista[i][j] == "a" or  lista[i][j] == "e" or lista[i][j] == "i" or lista[i][j] == "o" or lista[i][j] == "u":

            lista[i] = lista[i][j:] + lista[i][:j] + "ay"

            j = len(lista[i])+1

          else:

            j+=1

      i+=1


      string =" ".join(lista)

    return string


print(traducir_a_pig_latin("computer ahavales"))


    