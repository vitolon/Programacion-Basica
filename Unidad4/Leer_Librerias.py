from Archivos import guardar_diccionarios_en_csv
from Archivos import leer_diccionarios_de_csv
# Nombre del archivo a leer y de la función a importar
Nombres = {"juan", "Ana", "Luis"}
Edades = {25, 30, 35}
Ciudades = {"Madrid", "Barcelona", "Valencia"}

archivo = "datos.csv"
# Nombre del archivo
if __name__ == "__main__":
    datos = [
    {"Nombre": "Juan", "Edad": 25, "Ciudad": "Madrid"},
    {"Nombre": "Ana", "Edad": 30, "Ciudad": "Barcelona"},
    {"Nombre": "Luis", "Edad": 35, "Ciudad": "Valencia"}
]
#Diccionarios a guardar

# Guardar los diccionarios en un archivo csv
guardar_diccionarios_en_csv(archivo, datos)

# Actividad hacer un programa llamado LeerconLibreria.py que importe la función leer_diccionarios_de_csv y lea el archivo datos.csv
guardar_diccionarios_en_csv(archivo, datos)

    # Leer los diccionarios desde el archivo CSV
datos_leidos = leer_diccionarios_de_csv(archivo)
print("Datos leídos del archivo CSV:")
print(datos_leidos)