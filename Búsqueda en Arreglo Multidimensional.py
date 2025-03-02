# Programa Búsqueda en Arreglo Multidimensional

matriz = [
    [11, 12, 13],
    [41, 69, 70],
    [80, 88, 99]
]

# Función para buscar un valor en la matriz
def buscar_valor(matriz, valor):
    encontrado = False
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                encontrado = True
                print(f"Valor {valor} encontrado en la posición ({i+1}, {j+1})")
                break
        if encontrado:
            break
    if not encontrado:
        print(f"Valor {valor} no encontrado en la matriz")

# Valor a buscar
valor_buscar = 69

# Mostrar la matriz original
print("Matriz original:")
for fila in matriz:
    print(fila)

# Realizar la búsqueda
print("\nBuscando valor:", valor_buscar)
buscar_valor(matriz, valor_buscar)
