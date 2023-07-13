def crear_nodo(valor):

    return {'valor': valor, 'izq': None, 'der': None}

def arbol_primario(raiz, valor):

    if raiz is None:
        return crear_nodo(valor)

    if valor < raiz['valor']:
        raiz['izq'] = arbol_primario(raiz['izq'], valor)
    else:
        raiz['der'] = arbol_primario(raiz['der'], valor)

    return raiz

def arbol_secundario(raiz, valor):

    if raiz is None:
        return crear_nodo(valor)

    if valor < raiz['valor']:
        raiz['izq'] = arbol_secundario(raiz['izq'], valor)
    else:
        raiz['der'] = arbol_secundario(raiz['der'], valor)

    return raiz


def twin_trees(arr):

    if not arr:
        return {'raiz_primario': None, 'raiz_secundario': None}

    raiz_primario = crear_nodo(arr[0])
    for valor in arr[1:]:
        arbol_primario(raiz_primario, valor)

    arr.reverse()
    raiz_secundario = crear_nodo(arr[0])
    for valor in arr[1:]:
        arbol_secundario(raiz_secundario, valor)

    return {'raiz_primario': raiz_primario, 'raiz_secundario': raiz_secundario}

print(twin_trees([4,6,9,2,1,3,5,8]))