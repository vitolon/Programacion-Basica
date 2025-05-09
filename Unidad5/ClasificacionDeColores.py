import os
import time
import random 

colores = ["rojo", "azul", "verde"]

def Limpiar_el_Cochinero():
    os.system('cls' if os.name == 'nt' else 'clear') 

def detectar_color():
    colores = ["rojo", "verde", "azul"]
    return random.choice(colores)

def Banda_Transportadora():
    
    while True:
        print("detecto objeto")
        color = detectar_color()
        print(f"color detectado: {color.upper()}")
        if color == "rojo":
            print ("Se detecto objeto de color rojo")
            print ("Activando servo motor rojo")
            time.sleep(5)
        elif color == "verde":
            print ("Se detecto objeto de color verde")
            print ("Activando servo motor verde")
            time.sleep(5)
        elif color == "azul":
            print ( " se detecto objeto de color azul")
            print ("Activando servomotor azul")
            time.sleep(5)
        else:
            print ("Aun no se ah detectado ningun objeto")
            time.sleep(5)
if __name__ == "__main__":
    Limpiar_el_Cochinero()
    Banda_Transportadora()