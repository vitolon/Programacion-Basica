# Diccionarios2.py

# Crear un diccionario con más de dos valores por clave
estudiantes = {
    "Manuel": {"edad": 18, "carrera": "Ingeniería Mecatronica"},
    "Aaron": {"edad": 18, "carrera": "Ingeniería Mecatronica"},
    "Victor": {"edad": 18, "carrera": "Ingeniería Mecatronica"},
    "Alexa": {"edad": 18, "carrera": "Ingeniería Mecatronica"},
    "lupita": {"edad": 18, "carrera": "Ingeniería Mecatronica"},
    "Enrique": {"edad": 18, "carrera": "Ingeniería Mecatronica"},
    "Cristian": {"edad": 18, "carrera": "Ingeniería Mecatronica"},
    "Sabayd": {"edad": 19, "carrera": "Ingeniería Mecatronica"},
    "Roberto": {"edad": 18, "carrera": "Ingeniería Mecatronica"},
    "Oswaldo": {"edad": 18, "carrera": "Ingeniería Mecatronica"},
    "Adan": {"edad": 18, "carrera": "Ingeniería Mecatronica"},

}

# Imprimir el diccionario completo
print("Diccionario de estudiantes:")
for nombre, detalles in estudiantes.items():
    print(f"{nombre}: {detalles}")

