def busqueda_secuencial(lista, objetivo):
    for indice in range(len(lista)):
        if lista[indice] == objetivo:
            return f"Elemento encontrado en el índice: {indice}"
    
    return "El elemento no se encuentra en la lista"

mi_lista = [10, 45, 2, 33, 8]
print(busqueda_secuencial(mi_lista, 33))