# Ciclo while
from variables import estatura

# Calculadora índice masa corporal (IMC)

contador = 1  # Para que entre al bucle pidiendo datos

while contador != 2:

    contador = int(input("¿Quieres seguir calculando el IMC? 1.Sí / 2.No: "))

    if contador == 1:

        estatura = float(input("Ingrese su estatura en metros: "))
        peso = float(input("Ingrese su peso en kilogramos: "))
        resultado = round(peso / (estatura ** 2), 2)

        if resultado < 18.5:
            print(f"IMC {resultado} = BAJO DE PESO")

        elif 18.5 <= resultado < 25:
            print(f"IMC {resultado} = PESO NORMAL")

        elif 25 <= resultado < 30:
            print(f"IMC {resultado} = SOBREPESO")

        else:
            print(f"IMC {resultado} = OBESIDAD")

    elif contador == 2:
        print("Hasta pronto, gracias por usar la calculadora de IMC")
    else:
        print("Opción inválida")
