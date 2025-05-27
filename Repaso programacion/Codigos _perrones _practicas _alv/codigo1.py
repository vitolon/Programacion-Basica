Cables = ["dupont", "banana", "duple", "hdmi", "ethrnet", "usb", "micro_usb", "tipo_c"]
cable_a_buscar = input("ingrese el tipo de cable que busca: ").lower()

if cable_a_buscar in Cables:
    print(f"el cable {cable_a_buscar} si esta en el inventario")
else:
    print(f"el cable {cable_a_buscar}no esta en el inventario")
    
    
