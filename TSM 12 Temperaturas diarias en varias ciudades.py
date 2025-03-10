## Paso 1: Crear matriz 3D para temperaturas
# Dimensiones: [Ciudades][Días][Semanas]
temperaturas = [
    # Ciudad 1 (QUITO)
    [
        # Semana 1 (7 días)
        [22.5, 23.0, 24.1, 25.3, 20.8, 21.2, 19.5],
        # Semana 2
        [18.9, 19.5, 20.1, 23.4, 24.0, 22.7, 21.1]
    ],
    # Ciudad 2 (CUENCA)
    [
        # Semana 1
        [24.0, 25.1, 26.3, 23.7, 22.9, 24.5, 25.0],
        # Semana 2
        [20.1, 21.3, 19.8, 18.5, 20.9, 22.0, 23.1]
    ],
    # Ciudad 3 (GUAYAQUIL)
    [
        # Semana 1
        [29.0, 28.0, 28.0, 27.0, 29.0, 27.0, 29.0],
        # Semana 2
        [27.1, 28.8, 28.0, 29.5, 30.2, 29.9, 28.4]
    ]
]

## Paso 2 y 3: Calcular promedios
promedios = []

# Iterar por cada ciudad
for indice_ciudad, ciudad in enumerate(temperaturas):
    promedios_ciudad = []

    # Iterar por cada semana en la ciudad
    for indice_semana, semana in enumerate(ciudad):
        total = 0.0

        # Sumar temperaturas diarias
        for temperatura in semana:
            total += temperatura

        # Calcular y almacenar promedio
        promedio_semanal = total / len(semana)
        promedios_ciudad.append(promedio_semanal)

    promedios.append(promedios_ciudad)

## Paso 4: Mostrar resultados
nombres_ciudades = ["Madrid", "Barcelona", "Valencia"]

for indice_ciudad, ciudad in enumerate(promedios):
    print(f"\n=== {nombres_ciudades[indice_ciudad]} ===")

    for indice_semana, promedio in enumerate(ciudad):
        print(f"Semana {indice_semana + 1}: {promedio:.2f}°C")

