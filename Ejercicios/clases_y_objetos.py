# Clases y Objetos:

class Bicicleta:
    def __init__(self, color, cambios, rin):
        self.color = color
        self.cambios = cambios
        self.rin = rin

    def frenar(self):
        return "La bicicleta está frenando"

    def avanzar(self):
        return "La bicicleta está en movimiento"

    def girar(self):
        return "La bicicleta está girando"

urbana = Bicicleta(color = "blue", cambios = 5, rin = 27.5)
Híbrida = Bicicleta(color = "red", cambios = 1, rin = 29)

print(urbana.color)
print(urbana.girar())
print(urbana.frenar())
print(urbana.rin)
print(urbana.avanzar())

print("Urbana: " + str(urbana.color))
print("Comportamiento de la bicicleta urbana: " + str(urbana.girar()))










