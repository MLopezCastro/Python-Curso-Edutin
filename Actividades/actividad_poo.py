# Actividad 6 - Impuestos

class Persona:
    def __init__(self):
        self.nombre = input("Ingrese el nombre: ")
        self.edad = int(input("Ingrese la edad: "))

    def imprimir(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")


class Ciudadano(Persona):
    def __init__(self):
        super().__init__()  # hereda nombre y edad
        self.deposito = float(input("Ingrese el depósito en USD: "))

    def imprimir(self):
        super().imprimir()  # imprime nombre + edad
        print(f"Depósito: {self.deposito} USD")

    def impuestos(self):
        if self.deposito > 4000:
            print("Debe pagar impuestos.")
        else:
            print("NO debe pagar impuestos.")


# Crear el objeto y llamar métodos
ciudadano1 = Ciudadano()
ciudadano1.imprimir()
ciudadano1.impuestos()


"""
Evaluación de impuestos según los datos del ejercicio:

Nombre              Edad    Depósito   ¿Paga impuestos?
--------------------------------------------------------
Manuel Chima        25      6700       SI (depósito > 4000)
Fayle García        56      3500       NO  (depósito <= 4000)
Lesly Rodríguez     34      9000       SI (depósito > 4000)
Mario Herrera       45      2500       NO  (depósito <= 4000)
"""
