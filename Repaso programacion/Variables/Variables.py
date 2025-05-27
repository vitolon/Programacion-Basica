#Definiendo una variable con CamelCase.
NombreCompletoTuyoMiPerro = "tilin"

#Definiendo una varaible con snake_case.
nombre_completo_tuyo_mi_perro = "tilin"

#Concatenando cadenas de texto con +.
bienvenido = "Hola, bienvenido " + nombre_completo_tuyo_mi_perro + " ¿como estas?"
print(bienvenido)

#Concatenando con f-strings por que es mas facil de leer.
bienvenido = f"Hola, bienvenido {nombre_completo_tuyo_mi_perro} ¿como estas?"
print(bienvenido)

#Operadores de pertenencia.
print("tilin" in bienvenido) #True
print("tilin" not in bienvenido) #False