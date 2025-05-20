
def nombre_programa():
    print(f"hackaton6.2")
    return "Contador de Palabras"

def contar_palabras(texto):
    palabras = texto.split()
    cantidad_palabras = len(palabras)
    return cantidad_palabras

def main():
    nombre = nombre_programa()
    print(f"has iniciado el programa: {nombre}")
    texto_usuario = input("escribe una frase:" )
    cantidad_palabras =contar_palabras(texto_usuario)
    print(f"el texto contiene {cantidad_palabras} palabras")

if __name__ == "__main__":
    main()

