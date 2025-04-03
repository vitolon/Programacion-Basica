# Herencia
# Clase base o padre
class Personaje:
    def __init__(self, Nombre, Nivel, Salud):
        self.Nivel = Nivel
        self.Nombre = Nombre
        self.Salud = Salud
   
    def info_personaje (self):
        return f"Tu personaje de nombre {self.Nombre}, es nivel {self.Nivel}, Cuentas con {self.Salud} puntos de salud"
# Clase derivada o hija
class Guerrero(Personaje):
    def __init__(self, Nombre, Nivel, Salud, Cuerpo_a_Cuerpo, Mucho_daño):
        super().__init__(Nombre, Nivel, Salud)  # Llamada al constructor de la clase padre
        self.Ataque = Cuerpo_a_Cuerpo
        self.Daño = Mucho_daño
   
    def info_personaje (self):
        # Sobrescribimos el método de la clase padre
        return f"Tu personaje de nombre {self.Nombre}, es nivel {self.Nivel}, Cuentas con {self.Salud} puntos de salud, un Guerrero que ataca {self.Ataque} y hace {self.Daño}"

# Otra clase derivada
class Mago(Personaje):
    def __init__(self, Nombre, Nivel, Salud, Muy_Veloz, Larga_Distancia):
        super().__init__( Nombre, Nivel, Salud)
        self.Movilidad = Muy_Veloz
        self.Alcance = Larga_Distancia
    
    def info_personaje(self):
        return f"Tu personaje de nombre {self.Nombre}, es nivel {self.Nivel}, Cuentas con {self.Salud} puntos de salud, Mediante brincos tienes una movilidad  {self.Movilidad} y un alcanze de ataque {self.Alcance} "        

# Programa principal
if __name__ == "__main__":
    Personaje = Personaje("Geralt", 40, 250)
    Guerrero = Guerrero("Geralt", 40, 250, "a base de machetazos", "mucho daño")
    Mago = Mago("Yennifer",37, 100, "muy estupefacta","muy berraco,para que te des una idea: de aqui a las Animas " )

    print(Personaje.info_personaje())
    print(Guerrero.info_personaje())
    print(Mago.info_personaje())