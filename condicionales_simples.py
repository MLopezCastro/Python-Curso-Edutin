# Condicionales y Ciclos

# if, else, elif (condicionales)

"""
Crear un programa que reciba el número de años que tiene nuestra computadora.
Imprimir en consola si es nuevo a viejo.
Condiciones: Si es menor o igual a 2 años, entonces es nuevo.
Pero, si es mayor a 2 años, entonces es viejo.
"""

anios = int(input("¿Cuántos años tiene tu computadora?"))

if anios >= 0 and anios <= 2:
    print("Tu computadora es nueva.")
else:
    print("Tu computadora es vieja.")


edad = int(input("¿Cuántos años tienes?"))

if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")

print("¡Nos vemos!")







