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



#Divide y venceras

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


# 1,1,2,3,5,8,13,21,34,55,89,144...

def fibonacci(n):
    
    
    if n == 0 or n == 1:
        
        return n
    
    else:
        
        return fibonacci(n-1) + fibonacci(n-2)
    
print(fibonacci(12))

"""

lis = [2,5,3,4,7,56]

def mergeSort(lis,start,end):
    
    if start < end:
        
        mid = (start + end) // 2
        mergeSort(lis,0,mid)
        mergeSort(lis,mid+1,end)
        merge(lis,start,mid,end)
        
def merge(lis,start,mid,end):
    
    #build temp array to avoid modifying the original input array
    
    temp = [0 for k in range(0,lis[len(lis)-1])]
    
    i = start
    j = mid+1
    k = 0

    #While both sub-array have values, then try and merge them in sorted order
    while (i <= mid and j <= end):
        
        if lis[i] <= lis[j]:
        
            temp[k] = lis[i]
            
            k += 1
            i += 1
        else:
            
            temp[k] = lis[j]
            
            k += 1
            j += 1
           
    #Add the rest of the values from the left sub-array into the result        
    while i<= mid:
        
        temp[k] = lis[i]
        
        k += 1
        i += 1
        
    #Add the rest of the values from the right sub-array into the result        
    while j<= end:
        
        temp[k] = lis[j]
        
        k += 1
        i += 1
        
        
    for i in range(start,end):
        
        lis[i] = temp[i-start]



print(mergeSort(lis, 0, lis[len(lis)-1]))

    
    
"""
    
    
    
    
    
    
    
    
    
    
    
        
        


    










