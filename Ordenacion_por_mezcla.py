def merge_sort(lista):
    # Caso base: si la lista tiene 0 o 1 elementos, ya está ordenada
    if len(lista) <= 1:
        return lista

    # 1. DIVIDIR: Encontramos el medio y partimos la lista en dos
    medio = len(lista) // 2
    izquierda = lista[:medio]
    derecha = lista[medio:]

    # Llamada recursiva para seguir dividiendo
    izquierda = merge_sort(izquierda)
    derecha = merge_sort(derecha)

    # 2. VENCER (Mezclar): Combinamos las dos mitades ordenadas
    return mezclar(izquierda, derecha)

def mezclar(izq, der):
    resultado = []
    i = j = 0

    # Comparamos elementos de ambas mitades y agregamos el menor
    while i < len(izq) and j < len(der):
        if izq[i] < der[j]:
            resultado.append(izq[i])
            i += 1
        else:
            resultado.append(der[j])
            j += 1

    # Agregamos los elementos que hayan quedado sobrantes
    resultado.extend(izq[i:])
    resultado.extend(der[j:])
    
    return resultado

# Ejemplo de uso:
numeros = [38, 27, 43, 3, 9, 82, 10]
lista_ordenada = merge_sort(numeros)
print(f"Lista original: {numeros}")
print(f"Lista ordenada: {lista_ordenada}")
