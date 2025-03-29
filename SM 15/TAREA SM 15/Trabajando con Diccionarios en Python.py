# Trabajando con Diccionarios en Python
# PASO 1. Tarea crear un Diccionario
# Crea un diccionario llamado informacion_personal con información ficticia
informacion_personal = {
    "nombre": "Eddwin Noriega",
    "edad": 35,
    "ciudad": "Quito",
    # La clave "profesión" se agregará más adelante
}

# PASO 2. Acceder y Modificar Valores
# Accede al valor asociado con la clave "ciudad" y modifícalo
informacion_personal["ciudad"] = "San Miguel de Bolivar"

# Agrega una nueva clave-valor para representar la "profesión"
informacion_personal["profesión"] = "Estudiante de Tecnologias de la Informacion"

# 3. Verificar Existencia de Claves
# Verifica si la clave "teléfono" existe en el diccionario
if "teléfono" not in informacion_personal:
    # Si no existe, agrégala con un número de teléfono ficticio
    informacion_personal["teléfono"] = "0990937519"

# 4. Eliminar una Clave
# Elimina la clave "edad" del diccionario
del informacion_personal["edad"]

# 5. Imprimir el Diccionario Final
# Imprime el diccionario resultante después de realizar todas las operaciones
print("Información Personal Final:")
print(informacion_personal)

