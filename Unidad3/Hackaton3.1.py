# Hackaton3.1.py

def hacer_mandado():
    # Preguntar si el usuario desea realizar el mandado
    respuesta = input("¿Deseas realizar el mandado? (si/no): ").lower()
    
    if respuesta == 'si':
        # Preguntar cuántos artículos desea comprar
        cantidad_articulos = int(input("¿Cuántos artículos deseas comprar? "))
        
        # Lista para guardar los artículos
        articulos = []
        
        # Pedir los nombres de los artículos y guardarlos en la lista
        for i in range(cantidad_articulos):
            articulo = input(f"Ingresa el nombre del artículo {i+1}: ")
            articulos.append(articulo)
        
        # Imprimir la lista de artículos
        print("\nTu lista de mandados es:")
        for articulo in articulos:
            print(f"- {articulo}")
    else:
        print("Entendido, no se realizará el mandado.")

# Llamar a la función para ejecutar el programa
hacer_mandado()
















 