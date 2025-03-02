# Ordenación de Arreglo Multidimensional

# Definir la matriz bidimencional
matriz = [
    [6, 8, 11],
    [10, 2, 45],
    [7, 8, 99]
]

# Función para ordenar una fila de la matriz usando Bubble Sort
def ordenar_fila(matriz, fila):
    # Aplicar Bubble Sort a la fila especificada
    for i in range(len(matriz[fila])):
        for j in range(len(matriz[fila]) - 1):
            if matriz[fila][j] > matriz[fila][j + 1]:
                matriz[fila][j], matriz[fila][j + 1] = matriz[fila][j + 1], matriz[fila][j]
    return matriz

# Mostrar la matriz original
print("Matriz original:")
for fila in matriz:
    print(fila)

# Ordenar la segunda fila (índice 1)
print("\nOrdenando la segunda fila...")
matriz_ordenada = ordenar_fila(matriz, 1)

# Mostrar la matriz con la fila ordenada
print("Matriz con la segunda fila ordenada:")
for fila in matriz_ordenada:
    print(fila)
