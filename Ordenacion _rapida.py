def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    
    pivote = lista[len(lista) // 2]
    
    izquierda = [x for x in lista if x < pivote]
    centro    = [x for x in lista if x == pivote]
    derecha   = [x for x in lista if x > pivote]
    
    return quick_sort(izquierda) + centro + quick_sort(derecha)

datos = [23, 1, 15, 8, 5, 2]
print(f"Lista ordenada: {quick_sort(datos)}")