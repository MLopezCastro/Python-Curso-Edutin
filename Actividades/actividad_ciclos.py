# Solicitar información
nombre = input("Nombre completo: ")
materias = 5

# Hacer un ciclo, pedir datos y sumar la calificación
contador = 1
sumatoria = 0

while contador <= materias:
    nombre_materia = input(f"Ingresa el nombre de la materia {contador}: ")
    calificacion = float(input(f"Calificación obtenida en {nombre_materia}: "))

    # Sumar la calificación a la sumatoria
    sumatoria = sumatoria + calificacion

    # Aumentar el contador para no hacer un ciclo infinito
    contador = contador + 1

# Hacer cálculos e imprimir resultados
promedio = sumatoria / materias

print("\n*** RESULTADOS ***")
print(f"Hola, {nombre}, tienes un promedio de {promedio} en el 5to semestre.")
