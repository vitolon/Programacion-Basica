# Lista vacía para organizar los videojuegos.
import os #Esta libreria se importa para poder limpiar la pantalla y asi no se vea un cochinero en la pantalla.
import time #Se importa esta libreria para poder hacer pausas mientras se esta ejecutando el codigo

#Se crean los diccionarios, eso si, vacios ya que la intencion con este programa es preguntar por los videojuegos para despues decidir donde organizarlos.
Accion = {}
Aventura = {}
Terror = {}

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
    print("\n--- Agregar un juego ---")
    nombre = input("Ingresa el nombre del juego: ")
    genero = input("Ingresa el género del juego (Accion/Aventura/Terror): ").lower()#se utiliza lower para cambiar todo lo escrito a minusculas sin importar si se escribio con uso de mayuculas y minusculas

    if genero == "accion":
        Accion[nombre] = genero
        print(f"'{nombre}' ha sido agregado a la categoría 'Accion'.")
    elif genero == "aventura":
        Aventura[nombre] = genero
        print(f"'{nombre}' ha sido agregado a la categoría 'Aventura'.")
    elif genero == "terror":
        Terror[nombre] = genero
        print(f"'{nombre}' ha sido agregado a la categoría 'Terror'.")
    else:
        print("Género no disponible. Usa 'Accion', 'Aventura' o 'Terror'.")
        
    time.sleep(2)# Se da una espera de 2 segundos para continuar con la siguiente accion

#se eliminan juegos de los generos
def Eliminar_juego():
    print("\n--- Eliminar un juego ---")
    nombre = input("Ingresa el nombre del juego que quieres Eliminar ")

    if nombre in Accion :
        del Accion[nombre] 
        print(f"'{nombre}' ha sido eliminado de la categoría 'Accion'.")
    elif nombre in Aventura:
        del Aventura[nombre] 
        print(f"'{nombre}' ha sido eliminado de la categoría 'Aventura'.")
    elif nombre in Terror:
        del Terror[nombre] 
        print(f"'{nombre}' ha sido eliminado de la categoría 'Terror'.")
    else:
        print("No a sido encontrado en ninguna categoria")
    time.sleep(2)# Se da una espera de 2 segundos para continuar con la siguiente accion

#Se ven los juegos agregados en cada lista
def Mostrar_juegos():
#se visualizan los juegos ordenados en cada genero    
    print("\n---ver lista de juegos---")
#se checan los juegos que hay en Accion  
    print("\n---ver juegos en Accion---")
    if Accion:
        for nombre in Accion:
            print(f"-{nombre}")
    else:
        print("No hay juegos en este genero")
#se checan los juegos que hay en Aventura 
    print("\n---ver juegos en Aventuras---")
    if Aventura:
        for nombre in Aventura:
            print(f"-{nombre}")
    else:
        print("No hay juegos en este genero")
#se checan los juegos que hay en Terror        
    print("\n---ver juegos en Terror---")
    if Terror:
        for nombre in Terror:
            print(f"-{nombre}")
    else:
        print("No hay juegos en este genero")

    input("\nPresiona Enter para fokin continuar...")  # espera a que el insecto le de al fokin enter

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
            print("Opcion incorrecta, intente con otra")      
            time.sleep(2)


if __name__ == "__main__":
    main()
