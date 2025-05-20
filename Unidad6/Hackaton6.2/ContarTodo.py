palabra = input("escribe una palabra:")

contar_vocal = 0
contar_consonante = 0
contar_numeros = 0
contar_otros = 0
for letra in palabra.lower():
    if letra in "aeiou":
        contar_vocal += 1
    elif letra.isalpha():
        contar_consonante += 1
    elif letra.isdigit():
        contar_numeros += 1
    else:
        contar_otros += 1


print("la cantidad de vocales es: ",contar_vocal)
print("La cantidad de consonantes es:",contar_consonante)
print("La cantidad de numeros es :" ,contar_numeros)
print("la cantidad de ortos caracteres es :",contar_otros)