Proceso ClasificacionPorColor
	
    Definir color Como Cadena
    Definir objetoDetectado Como Logico
	
   
    Escribir "Sistema de Clasificación por Color Iniciado"
	
    Repetir
   
        Escribir "¿Objeto detectado? (1 = si, 0 = no): "
        Leer objetoDetectado
		
        Si objetoDetectado Entonces
			
            Esperar 1 segundos
           
            Escribir "Ingrese el color del objeto (rojo, verde, azul): "
            Leer color
			
           
            Si color = "rojo" Entonces
                Escribir "poniendolo con,los rojos"
				
			Sino
				Si color = "verde" Entonces
                Escribir "poniendolo con los verdes"
				
			Sino
				Si color = "azul" Entonces
                Escribir "poniendolo con los azules"
				
            Sino
                Escribir "Color desconocido."
				
            FinSi
			
            Esperar 1 Segundos 
            Escribir "Servomotor vuelve a posición inicial"
			
        FinSi
	FinSi
FinSi

    Hasta Que Falso 
FinProceso