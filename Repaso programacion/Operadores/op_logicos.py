#AND
resultado = 2<3 and 3<4  #da verdadero 
resultado2 = 2<3 and 3>4 #da falso
resultado3 = 2>3 and 3<4 #da falso
resultado4 = 2>3 and 3>4  #da falso

#print(resultado)
#print(resultado2)
#print(resultado3)
#print(resultado4)

#OR

resultado5 = 4 == 4 or 2 == 2  #da verdadero
resultado6 = 4 == 4 or 2 != 2 #da verdadero
resultado7 = 3<2 or 1<2 #da verdadero
resultado8 = 1>2 or 3>4 #da falso

#print(resultado5)
#print(resultado6)
#print(resultado7)
#print(resultado8)

#NOT

resultado9 = not 2 == 2 #da falso
resultado10 = not 1>2 #da verdadero

#print(resultado9)
#print(resultado10)