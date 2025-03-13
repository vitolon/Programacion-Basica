# Programacion basica
## Victor Manuel Ontiveros Mares
## Subtitulos
### Unidad 1
- ¿Que es un paradigma de programacion? 
Un paradigma de programación es un enfoque o estilo que se utiliza para diseñar y estructurar programas. Define cómo se organiza el código y cómo se resuelven los problemas. Los paradigmas más comunes son: Programación estructurada: Se enfoca en dividir el código en funciones o procedimientos para mejorar la claridad y el mantenimiento. Programación orientada a objetos (POO): Organiza el código en "objetos" que contienen datos (atributos) y comportamientos (métodos). Ejemplos: Python, Java, C++. Programación funcional: Trata la programación como la evaluación de funciones matemáticas, evitando el uso de estados y datos mutables. Ejemplos: Haskell, Erlang. Programación imperativa: Describe cómo se debe realizar una tarea paso a paso. Ejemplos: C, Pascal. Programación declarativa: Se enfoca en describir qué se debe hacer, en lugar de cómo hacerlo. Ejemplos: SQL, Prolog. Cada paradigma tiene sus ventajas y se elige según el problema a resolver.

- ¿Que son los operadores?
Los operadores son símbolos o palabras clave que realizan operaciones sobre uno o más valores (llamados operandos). Se clasifican en varios tipos:

Operadores aritméticos: Realizan operaciones matemáticas.

Ejemplos: + (suma), - (resta), * (multiplicación), / (división), % (módulo), ** (exponenciación).

Operadores de comparación: Comparan dos valores y devuelven un valor booleano (True o False).

Ejemplos: == (igual a), != (diferente de), > (mayor que), < (menor que), >= (mayor o igual que), <= (menor o igual que).

Operadores lógicos: Combinan expresiones booleanas.

Ejemplos: and (y lógico), or (o lógico), not (negación).

Operadores de asignación: Asignan valores a variables.

Ejemplos: = (asignación), += (suma y asignación), -= (resta y asignación).

Operadores de identidad: Comparan si dos objetos son el mismo.

Ejemplos: is, is not.

Operadores de pertenencia: Verifican si un valor está presente en una secuencia.

Ejemplos: in, not in.

Operadores a nivel de bits: Realizan operaciones sobre bits.

Ejemplos: & (AND), | (OR), ^ (XOR), ~ (NOT), << (desplazamiento a la izquierda), >> (desplazamiento a la derecha).

- ¿Que es un lenguaje de bajo nivel y de alto nivel?
Lenguaje de bajo nivel:
Definición: Son lenguajes más cercanos al hardware de la computadora. Están diseñados para interactuar directamente con el procesador y la memoria.

Características:

Cercanía al hardware: Permiten un control preciso sobre el sistema.

Dificultad: Son más difíciles de aprender y usar porque requieren conocimiento del hardware.

Ejemplos: Lenguaje ensamblador (Assembly) y código máquina.

Uso: Se utilizan en sistemas embebidos, desarrollo de sistemas operativos y aplicaciones que requieren alto rendimiento.

Lenguaje de alto nivel:
Definición: Son lenguajes más cercanos al lenguaje humano y están diseñados para ser fáciles de leer y escribir.

Características:

Abstracción: No requieren conocimiento del hardware.

Facilidad: Son más fáciles de aprender y usar.

Portabilidad: El código puede ejecutarse en diferentes plataformas con pocos o ningún cambio.

Ejemplos: Python, Java, C#, JavaScript, Ruby.

Uso: Desarrollo de aplicaciones web, móviles, de escritorio, inteligencia artificial, etc.

### Unidad 2
operadores:
 1. if: el codigo if sirve para comparar respuestas, si se cumple lo que indica el if, entonces se puede ejecutar a siguiete funcion.
 
 if numero > 0:
    print("El número es positivo.")

 2. else: El else se ejecuta cuando no se ejecuta cuando no se cunple la funcion del if.

elif numero < 0:
    print("El número es negativo.")

 3. elif: nos puede indicar lo contrario al if, osea que si el if nos dice que es mayor a 1, elif nos indica si es menor que 1.

else:
    print("El número es cero.")

 4. while: while es una condicion que solo se ejecuta en caso de ser cierta la funcion a la que esta referida.

 contador = 0

while contador < 5:
    print(f"El contador es: {contador}")
    contador += 1

print("El bucle while ha terminado.")

5. for: son ciclos que se repiten hasta cumplir cierto objetivo, por ejemplo si el for es 5 y nuestro contador empieza desde 1 entonces se seguira repitiendo hasta que se cumpla el objetivo del for que es 5.

for nombre in nombres:
    print(nombre)

6. librerias: Librerias son aquellas que nos ayudan para realizar distintas funciones, por ejemplo la libreria math nos sirve para hacer muchas opercoiones matematicas.

import math

print(math.sqrt(25))

7. Tipos de datos: estos son las formas de organizarse de los datos que se ponen en los codigos por ejemplo estan los datos enteros, flotantes, complejos, en cadena y los booleanos.

entero = 5
flotante = 1.2
cadena = "Ed Flores"
booleano = True

8. Switch(programacion): este nos sirve para separar en varias opciones y que el usuario pueda elegir uno como si de switches se tratara

def switch_example(option):
    switcher = {
        1: "Option 1 selected",
        2: "Option 2 selected",
        3: "Option 3 selected",
 }


a = 10
b = 3
9. suma = a + b      # 10 + 3 = 13
10. resta = a - b     # 10 - 3 = 7
11. multiplicacion = a * b  # 10 * 3 = 30
12. division = a / b  # 10 / 3 = 3.333...
13. division_entera = a // b  # 10 // 3 = 3
14. potencia = a ** b  # 10^3 = 1000´


### Unidad 3
listas: son conjuntos de datos ya dependiendo de como lo organicemos, podemos dejarlas vacias paara posterior mente con ayuda de algunas funciones les agreguemos datos o desde un inicio ponerle datos dentro y posteriormente llamarlos e imprimirlos con algunas funciones.
Diccionarios: 
