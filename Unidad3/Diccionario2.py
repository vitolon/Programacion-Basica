Profesores = {
    "Eduardo": { "Materia": "Programacion basica", "promedio": 31},
    "Adilene": { "Materia": "Inglish", "promedio": 93},
    "Guillermo": { "Materia": "probabilidad", "promedio": 90},
    "Enrique": { "Materia": "Ingenieria de los materiales", "promedio": 88},
    "Marlem": { "Materia": "Calculo Integral", "promedio": 95},
    "Laura": { "Materia": "Administracion y Contabilidad", "promedio": 95},
    "Jorge": { "Materia": "Algebra lineal", "promedio": 0},

}

# Imprimir el diccionario completo
print("Diccionario de Profesores:")
for nombre, detalles in Profesores.items():
    print(f"{nombre}: {detalles}")
