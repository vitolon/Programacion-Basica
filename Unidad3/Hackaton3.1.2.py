# Lista para guardar los artículos
listaMandado = []

while True:
    # Preguntar si desea crear la lista del mandado
    respuesta = input("¿Deseas crear lista del mandado? (si/no): ").lower()

    if respuesta != 'si':
        print("Gracias, vuelve pronto.")
        break  # Salir del bucle si la respuesta no es 'si'

    # Preguntar cuántos productos desea comprar
    cantidad = int(input("¿Cuántos productos deseas comprar? "))

    # Pedir los nombres de los productos y guardarlos en la lista
    for i in range(cantidad):
        articulo = input(f"Ingresa el artículo {i + 1}: ").strip()
        listaMandado.append(articulo)
        print(f"✅ Artículo '{articulo}' agregado.")

    # Imprimir la lista de artículos
    print("\nLista de artículos a comprar:")
    for articulo in listaMandado:
        print(f"- {articulo}")

    # Preguntar si desea agregar más artículos
    continuar = input("¿Deseas agregar más artículos? (si/no): ").lower()
    if continuar != 'si':
        print("Gracias, tu lista de mandado está lista.")
        break  # Salir del bucle si no desea agregar más artículos