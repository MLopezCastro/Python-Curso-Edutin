"""
En una escuela de conducción se tiene un programa que dependiendo de la edad del ususario debe mostrar el tipo de licencia a la que tiene derecho.
Condición 1: si es menor a 16, entonces no puedes conducir.
Condición 2: si es menor a 18, entonces puedes obtener un permiso para conducir.
Condición 3: si es menor a 70, entonces puedes obtener una licencia estandar.
Condición 4: si es mayor a 70, entonces necesitas una licencia especial.
"""

edad = int(input("Ingrese su edad: "))
if edad < 16:
    print("No tienes edad para conducir.")
elif edad < 18:
    print("Puedes obtener un permiso para conducir.")
elif edad < 70:
    print("Puedes obtener una licencia estandar.")
else:
    print("Necesitas una 61licencia especial.")
