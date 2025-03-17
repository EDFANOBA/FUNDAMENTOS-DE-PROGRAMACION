# temperatura_app.py
# Definición y uso de funciones en programación
def calcular_promedios_temperaturas_ciudades(datos_temperaturas, lista_ciudades):
    """
    se calculara el promedio de temperaturas para cada ciudad considerando todas las semanas

    Args:
        datos_temperaturas (list): Matriz 3D con estructura [ciudades][semanas][días]
        lista_ciudades (list): Nombres de las ciudades correspondientes a la primera dimensión

    Returns:
        dict: Diccionario con {ciudad: promedio}
    """
    promedios = {}

    for indice_ciudad, ciudad in enumerate(lista_ciudades):
        total_temp = 0
        total_dias = 0

        # Iterar semanas y días
        for semana in datos_temperaturas[indice_ciudad]:
            for temperatura in semana:
                total_temp += temperatura
                total_dias += 1

        promedios[ciudad] = round(total_temp / total_dias, 1)

    return promedios


# Datos de ejemplo para 3 ciudades x 4 semanas x 7 días
temperaturas = [
    # Quito
    [
        [22.5, 23.0, 24.1, 25.3, 20.8, 21.2, 19.5], # semana 1
        [18.9, 19.5, 20.1, 23.4, 24.0, 22.7, 21,1], # semana 2
        [16.9, 18.8, 14.1, 18.4, 19.0, 19.2, 18.7], # semana 3
        [16.5, 117.5, 12.2, 14.3, 22.1, 17.9, 15.3] # semana 4
    ],
    # Cuenca
    [
        [20.0, 25.1, 26.3, 23.7, 22.9, 24.5, 25.0], # semana 1
        [20.1, 21.3, 19.8, 18.5, 20.9, 22.0, 23.1], # semana 2
        [19.5, 18.0, 21.5, 21.7, 20.0, 20.8, 14.0], # semana 3
        [14.5, 16.7, 12.9, 21.0, 22.3, 18.5, 16.7]  # semana 4
    ],
    # Guayaquil
    [
        [29.8, 28.0, 28.0, 27.0, 29.0, 27.0, 29.0], # semana 1
        [27.1, 28.8, 28.0, 29.5, 30.2, 29.9, 28.4], # semana 2
        [26.1, 29.7, 28.2, 29.9, 26.7, 28.3, 28.4], # semana 3
        [27.2, 28.4, 29.3, 32.9, 33.7, 29.5, 30.6]  # semana 4
    ]
]

nombres_ciudades = ["Quito", "Cuenca", "Guayaquil"]

# ejecutamos la respectiva prueba
# llamando a la funcion para calcaular a la temperatura promedio
# Prueba de la función
if __name__ == "__main__":
    resultados = calcular_promedios_temperaturas_ciudades(temperaturas, nombres_ciudades)

    print("=== Resultados de temperaturas promedio ===")
    for ciudad, promedio in resultados.items():
        print(f"{ciudad.ljust(10)}: {promedio}°C")
