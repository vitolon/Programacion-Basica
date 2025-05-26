#las listas son mutables, es decir que se puede cambiar su cpntenido
lista = ["mecatronica", 18, True, "chupas"]
#las tuplas son inmutables, es decir que no se puede cambbiar su contenido
tupla = ("mecatronica", 18, True, "chupas")

lista[3] = "azxs"  # Esto es válido porque las listas son mutables.
#tupla[3] = "azxs"  Esto generará un error porque las tuplas son inmutables.

print(lista[3])
print(tupla[3])

conjunto = {"mecatronica", 18, True, "chupas"}  # Esto es un conjunto, no se puede acceder por índice.
# Los conjuntos no tienen un orden específico y no permiten duplicados.

print(conjunto)

diccionario = {
    "carrera": "mecatronica",
    "edad": 18,
    "es_estudiante": True,
    "apodo": "chupas"
}  # Esto es un diccionario, se accede por clave.
print(diccionario["apodo"])  # se esta accediendo al valor asociado a la clave "apodo".

