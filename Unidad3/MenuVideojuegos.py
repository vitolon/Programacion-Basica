# Lista vacía para organizar los videojuegos.
import os #Esta libreria se importa para poder limpiar la pantalla y asi no se vea un cochinero en la pantalla.
import time #Se importa esta libreria para poder hacer pausas mientras se esta ejecutando el codigo
from Archivos import guardar_diccionarios_en_csv
from  Archivos import leer_diccionarios_de_csv
#Se crean los diccionarios, eso si, vacios ya que la intencion con este programa es preguntar por los videojuegos para despues decidir donde organizarlos.
Accion = [
    {"Nombre" : "pou"}
]
Aventura = {}
Terror = {}
Arcade ={}
Deportes = {}
Estrategia = {}
Simulacion = {}
Shooters = {}
#  se verifica el sistema operativo y se limpia la pantalla
def Limpiar_el_Cochinero():
    os.system('cls' if os.name == 'nt' else 'clear') 

def Mostrar_menu():
    print("1. Agregar Juego")
    print("2. Eliminar juego")
    print("3. Ver lista de juegos")
    print("4. Salir")
#se agregan juegos a los diccionarios

def Agregar_juego():
    print("\n Agregar un juego")
    nombre = input("Ingresa el nombre del juego: ")
    genero = input("Ingresa el género del juego (Accion, Aventura, Terror, Arcade, Deportes, Estrategia, Simulacion, Shooters): ").lower() #se utiliza lower para cambiar todo lo escrito a minusculas sin importar si se escribio con uso de mayuculas y minusculas

    if genero == "accion":#Cuando el morro que le mueve ingresa el nombre y el género de un juego, el código verifica gracias al 'if' si el género es "accion". Si es así, agrega el juego al diccionario de Accion y luego imrpimea un mensaje confirmando que el juego se ah agregado a ese diccionario.
        Accion[nombre] = genero
        print(f"'{nombre}' ha sido agregado a la categoría 'Accion'.")
    elif genero == "aventura":
        Aventura[nombre] = genero
        print(f"'{nombre}' ha sido agregado a la categoría 'Aventura'.")
    elif genero == "terror":
        Terror[nombre] = genero
        print(f"'{nombre}' ha sido agregado a la categoría 'Terror'.")
    elif genero == "arcade":
        Arcade[nombre] = genero
        print(f"'{nombre}' ha sido agregado a la categoria 'Arcade'.")
    elif genero == "deportes":
        Deportes[nombre] = genero
        print(f"'{nombre}' ha sido agregado a la categoria 'Deportes'.")
    elif genero == "estrategia":
        Estrategia[nombre] = genero
        print(f"'{nombre}' ha sido agregado a la categoria 'Estrategia'.")
    elif genero == "simulacion":
        Simulacion[nombre] = genero
        print(f"'{nombre}' ha sido agregado a la categoria 'Simulacion'.")
    elif genero == "shooters":
        Shooters[nombre] = genero
        print(f"'{nombre}' ha sido agregado a la categoria 'Shooters'.")    
    else:
        print("Género no disponible, prueba con: 'Accion', 'Aventura', 'Terror', 'Arcade', 'Deportes', 'Estrategia', 'Simulacion', 'Shooters'.")
        
    time.sleep(2)# Se da una espera de 2 segundos para continuar con la siguiente accion

#se eliminan juegos de los generos
def Eliminar_juego():
    print("\n Eliminar un juego")
    nombre = input("Ingresa el nombre del juego que quieres Eliminar ")

    if nombre in Accion :
        del Accion[nombre]
        print(f"'{nombre}' ha sido eliminado de la categoría 'Accion'.")# si el nombre esta en el diccionario pasa a eliminarlo del diccionario y despues imprime que se ah elimiado.
    elif nombre in Aventura:
        del Aventura[nombre] 
        print(f"'{nombre}' ha sido eliminado de la categoría 'Aventura'.")
    elif nombre in Terror:
        del Terror[nombre] 
        print(f"'{nombre}' ha sido eliminado de la categoría 'Terror'.")
    elif nombre in Arcade:
        del Arcade[nombre] 
        print(f"'{nombre}' ha sido eliminado de la categoría 'Arcade'.")
    elif nombre in Deportes:
        del Deportes[nombre] 
        print(f"'{nombre}' ha sido eliminado de la categoría 'Deportes'.")
    elif nombre in Estrategia:
        del Estrategia[nombre] 
        print(f"'{nombre}' ha sido eliminado de la categoría 'Estrategia'.")
    elif nombre in Simulacion:
        del Simulacion[nombre] 
        print(f"'{nombre}' ha sido eliminado de la categoría 'Simulacion'.")
    elif nombre in Shooters:
        del Shooters[nombre] 
        print(f"'{nombre}' ha sido eliminado de la categoría 'Shooters'.")
    else:
        print("No a sido encontrado en ninguna categoria")
    time.sleep(2)# Se da una espera de 2 segundos para continuar con la siguiente accion

#Se ven los juegos agregados en cada lista
def Mostrar_juegos():
#se visualizan los juegos ordenados en cada genero    
    print("\n ver lista de juegos")
#se checan los juegos que hay en Accion  
    print("\n juegos en Accion")
    if Accion:
        for nombre in Accion:
            print(f"-{nombre}")#lo que hace es checar si el diccionario tiene valores, si es haci, se interpreta la siguiente linea que es el for y lo qe hace basicamenrte es imprimier todos los nombes que estasn en el diccionario.
    else:
        print("No hay juegos en este genero")
#se checan los juegos que hay en Aventura 
    print("\n juegos en Aventuras")
    if Aventura:
        for nombre in Aventura:
            print(f"-{nombre}")
    else:
        print("No hay juegos en este genero")
#se checan los juegos que hay en Terror        
    print("\n juegos en Terror ")
    if Terror:
        for nombre in Terror:
            print(f"-{nombre}")
    else:
        print("No hay juegos en este genero")
#se checan los juegos que hay en Arcade
    print("\n juegos en Arcade")
    if Arcade:
        for nombre in Arcade:
            print(f"-{nombre}")
    else:
        print("No hay juegos en este genero")
#se checan los juegos que hay en Deportes
    print("\n juegos en Deportes")
    if Deportes:
        for nombre in Deportes:
            print(f"-{nombre}")
    else:
        print("No hay juegos en este genero")
#se checan los juegos que hay en Estrategia
    print("\n juegos en Estrategia")
    if Estrategia:
        for nombre in Estrategia:
            print(f"-{nombre}")
    else:
        print("No hay juegos en este genero")
#se checan los juegos que hay en Simulacion
    print("\n juegos en Simulacion")
    if Simulacion:
        for nombre in Simulacion:
            print(f"-{nombre}")
    else:
        print("No hay juegos en este genero")
#se checan los juegos que hay en Shooters
    print("\n juegos en Shooters")
    if Shooters:
        for nombre in Shooters:
            print(f"-{nombre}")
    else:
        print("No hay juegos en este genero")

    input("\nPresiona Enter para fokin continuar...plis:)")  # espera a que el insecto le de al fokin enter

def main():
    while True:
        Limpiar_el_Cochinero()
        Mostrar_menu()
        opcion = input("Selecciona una opcion (1-4):")

        if opcion == "1":
            Agregar_juego()#mandamos traer a la funcion que pusimos para agrgar juegos a los diccionarios
        elif opcion == "2":
            Eliminar_juego()#mandamos traer a la funcion que pusimos para eliminar juegos de los diccionarios
        elif opcion == "3":
            Mostrar_juegos()#mandamos a traer a la funcion que pusimos para ver los juegos que tiene cada diccionario
        elif opcion == "4":
            print("Gracias mai, te la lavas")
            break#se break el ciclo y tan tan.
        else:
            print("Esa ni existe, calale con otra hermano")      
            time.sleep(2)

if __name__ == "__main__":
    main()  # Aquí el usuario interactúa con el programa
    
    # Después de salir, guardamos los datos
    Datos = [
    {"Nombre": "Juan", "Edad": 25, "Ciudad": "Madrid"},
    {"Nombre": "Ana", "Edad": 30, "Ciudad": "Barcelona"},
    {"Nombre": "Luis", "Edad": 35, "Ciudad": "Valencia"}
    ]
    
    archivo = "Menu_juegos.py"
    
    guardar_diccionarios_en_csv(archivo, Accion)
    datos_leidos = leer_diccionarios_de_csv(archivo)
    print("Datos leídos del archivo CSV:")
    print(datos_leidos)