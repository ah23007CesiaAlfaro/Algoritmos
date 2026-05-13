def busqueda_simple(lista, objetivo):
    inicio = 0
    fin = len(lista) - 1

    while inicio <= fin:
        mitad = (inicio + fin) // 2  
        
        if lista[mitad] == objetivo:
            return f"¡Lo encontré! Está en la posición {mitad}"
        
        if lista[mitad] < objetivo:
            inicio = mitad + 1  
        else:
            fin = mitad - 1     

    return "No está en la lista"


numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(busqueda_simple(numeros, 3))

