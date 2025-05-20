
def contar_vocales(texto):
    cantidad_vocales = 0
    for caracter in texto.lower():
        if caracter in {'a', 'e', 'i', 'o', 'u'}:
            cantidad_vocales += 1
    return cantidad_vocales

def contar_consonantes(texto):
    cantidad_consonantes = 0
    for caracter in texto.lower():
        if caracter.isalpha() and caracter not in {'a', 'e', 'i', 'o', 'u'}:
            cantidad_consonantes += 1
    return cantidad_consonantes

def contar_numeros(texto):
    cantidad_numeros = 0
    for caracter in texto:
        if caracter.isdigit():
            cantidad_numeros += 1
    return cantidad_numeros

def contar_otros(texto):
    cantidad_otros = 0
    for caracter in texto:
        if not caracter.isalpha() and not caracter.isdigit() and not caracter.isspace():
            cantidad_otros += 1
    return cantidad_otros

def main():
    texto = input("Escribe una frase: ")
    cantidad_vocales = contar_vocales(texto)
    cantidad_consonantes = contar_consonantes(texto)
    cantidad_numeros = contar_numeros(texto)
    cantidad_otros = contar_otros(texto)
    
    print(f"El texto contiene {cantidad_vocales} vocales")
    print(f"El texto contiene {cantidad_consonantes} consonantes")
    print(f"El texto contiene {cantidad_numeros} números")
    print(f"El texto contiene {cantidad_otros} otros caracteres")

if __name__ == "__main__":
    main()