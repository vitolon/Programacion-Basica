Algoritmo sin_titulo
	Definir llave_abierta Como logico
	Definir humedad_actual como Real
	Definir humedad_minima Como Real
	Definir tiempo Como Entero
	
	humedad_minima <- 30.0
	tiempo <- 5
	
	Escribir "ingrese la humedad_actual"
	Leer humedad_actual
	
Si humedad_actual < humedad_minima Entonces
	llave_abierta = Verdadero
	Escribir "Humedad baja (",humedad_actual ,"%) activando llave por (", tiempo ,") segundos"
	Esperar tiempo Segundos
SiNo
	llave_abierta = Falso
	Escribir "parametros de humedad (" , humedad_actual, "%) normales, llave cerrada"
		
FinSi
	
		
FinAlgoritmo




#codigo con menu

Algoritmo sin_titulo
	
	Definir llave_abierta Como logico
	Definir humedad_actual como Real
	Definir humedad_minima Como Real
	Definir tiempo Como Entero
	
	humedad_minima <- 30.0
	
	Definir menu Como Caracter
	Escribir " MENU "
	Escribir "(1) opcion 1"
	Escribir "(2) opcion2"
	Leer menu
		
			
	Segun menu Hacer
		"1":
			Limpiar Pantalla
			Escribir ""
			Escribir "ponga aqui el tiempo que durara abierta la llavesona perrona"
			Leer tiempo
			Escribir "pulsa una tecla para continuar"
			Esperar Tecla
			
		"2":
			Limpiar Pantalla
			Escribir""
			Escribir "ponga aqui la humedad que tendra al iniciar"
			Leer humedad_actual 
			Escribir "pulsa una tecla para continuar"
			Esperar Tecla
			
			Si humedad_actual <= humedad_minima Entonces
				llave_abierta = Verdadero
				Escribir "Humedad baja (",humedad_actual ,"%) activando llave por (", tiempo ,") segundos"
				Esperar tiempo Segundos
			SiNo
				llave_abierta = Falso
				Escribir "parametros de humedad (" , humedad_actual, "%) normales, llave cerrada"
				Escribir "pulsa una tecla para continuar"
				Esperar Tecla
			FinSi
		"0":
			Escribir ""
			Escribir "Adio"
		De Otro Modo:
			Limpiar Pantalla
			Escribir menu, "no es una opcion que se pueda paps"
			Escribir "pulsa una tecla para continuar"
			Esperar Tecla
		
		
	FinSegun

		
FinAlgoritmo
