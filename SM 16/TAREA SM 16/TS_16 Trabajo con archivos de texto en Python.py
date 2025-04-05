# TAREA SEMANA 16
# En esta tarea, se realizara operaciones de lectura y escritura

# PASO 1. Escritura de Archivo de Texto
def escribir_archivo():

    # Abrir el archivo en modo escritura ('w')
    archivo = open("my_notes.txt", "w")

    # Escribe al menos tres líneas de notas personales
    notas = [
        "Nota 1: Proxima semana examenes parcial 2.\n",
        "Nota 2: Entrega tope de tareas domingo 23:59.\n",
        "Nota 3: Miercoles presentacion en el trabajo a las 07:00.\n"
    ]

    # Utiliza write() para escribir cada nota
    archivo.write(notas[0])
    archivo.write(notas[1])
    archivo.write(notas[2])

    # Cierra el archivo
    archivo.close()


# PASO 2. Lectura de Archivo de Texto
def leer_archivo():

    # Abrir el archivo en modo lectura ('r')
    archivo = open("my_notes.txt", "r")

    # Se lee el contenido línea por línea utilizando readline()
    while True:
        linea = archivo.readline()
        if not linea:
            break

        # Se muestra cada línea en la consola
        print(linea, end='')

    # se cierra el archivo
    archivo.close()

# Instrucciones principales
if __name__ == "__main__":
    # Primero, escribe en el archivo
    escribir_archivo()

    # Luego, lee el archivo
    leer_archivo()

