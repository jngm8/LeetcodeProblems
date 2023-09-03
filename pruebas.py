libros = [50,100,50,100]
def totalPaginas(libros):
    
    if len(libros) == 1:
        
        return libros[0]
    
    return libros[0] + totalPaginas(libros[1:])
print(totalPaginas(libros))
def factorial(num):
       
    if num == 1:
        
        return 1
        
    else:
        
       return num * factorial(num-1)
print(factorial(5))
def reversedString(pala:str)->str:
    
    
    if pala == "":
        
        return pala
    
    else:
        
        return reversedString(pala[1:]) + pala[0] 
print(reversedString("hello"))
def sumaAnteriores(numero):


    if numero <= 1:
        
        return numero
    
    
    else:
        
        
        return numero + sumaAnteriores(numero-1) 
print(sumaAnteriores(5))
lista = [0,1,2,3,4,5,6,7,8,9]
def binarySearch(lista,left,right,x):
    
    if left > right:
        
        return -1
    
    medio = (left + right) // 2
    
    if x == lista[medio]:
        
        return medio
    
    if x < lista[medio]:
        
        return binarySearch(lista, left, medio-1, x)
    
        
    return binarySearch(lista, medio+1, right, x)   
print(binarySearch(lista, lista[0], lista[len(lista)-1], 3))
def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)









