Nombres = ["lupita", "Sabayd", "Alexa", "Aaron", "Manuel", "Victor", "Cristian", "Enrique", "Roberto", "Oswaldo", "Adan" ]

Edades = [18, 20, 19, 18, 18, 19, 19, 19, 18 ]

Videojuegos =  ["Doom", "Minecraft", "Halo", "DMC", "Hollow knigth", "fifa", "Fornite", "Roblox", "Assasins Creed", "The witcher","DEad space", "Red dead redemption", "Cod",]

Materias = ["Calculo", "Algebra", "Contabilidad", "Estadistica", "Programacion", "Materiales", "Ingles"]

Profesores = ["Adilene", "Guillermo", "Laura", "Eduardo", "Enrique", "Marlen"]
#Imprimir las listas
print(Nombres)
print(Edades)
print(Videojuegos)
print(Materias)
print(Profesores)
#Imprimir el numero de datos que contiene cada lista
print(len(Nombres))
print(len(Edades))
print(len(Videojuegos))
print(len(Materias))
print(len(Profesores))
#Imprimir datos menores y mayores de la lista
print(max(Edades))
print(min(Edades))
#Remover algun elemento de una lista
Materias.remove("Programacion")
print(Materias)
#Agregar un elemento a una lista
Materias.append("Programacion xd")
print(Materias)
Materias.insert (1, "Programacion avanzada")
print(Materias)
#For
for Materia in Materias: 
    print(Materia)



