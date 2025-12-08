class Vehiculo:
    def __init__(self, matricula, modelo, marca, color):
        self.matricula = matricula
        self.modelo = modelo
        self.marca = marca
        self.color = color
        self.avanza = False
        self.frena = False
        self.gira = False

    def avanzar(self):
        self.avanza = True

    def frenar(self):
        self.frena = True

    def girar(self):
        self.gira = True

    def imprimir(self):
        print(f"Matricula: {self.matricula}")
        print(f"Modelo: {self.modelo}")
        print(f"Marca: {self.marca}")
        print(f"Color: {self.color}")
        print(f"Avanzando: {self.avanza}")
        print(f"Frenando: {self.frena}")
        print(f"Girando: {self.gira}")


class Moto(Vehiculo):
    def __init__(self, matricula, modelo, marca, color, cilindraje):
        super().__init__(matricula, modelo, marca, color)
        self.cilindraje = cilindraje


moto1 = Moto("ABC123", 2018, "BMW", "Rojo", 150)
moto1.avanzar()
moto1.girar()
moto1.frenar()
moto1.imprimir()
print("Cilindraje:", moto1.cilindraje)






