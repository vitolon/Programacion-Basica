contraseña = "VivaAMLO"
contraseña_insertada = input("contraseña: ")
nombre_usuario = "amlo"

if contraseña_insertada == contraseña:
    print("la contraseña es correcta")
    if contraseña_insertada == "VivaAMLO":
        usuario = input("Ingrese su nombre de usuario:")
        if usuario == nombre_usuario:
            print("bienvenido amlo")
        else:
            print("ususario incorrecto")
else:
    print("contraseña incorrecta, intente de nuevo")    
# El código verifica si la contraseña ingresada es correcta y luego valida el nombre de usuario.