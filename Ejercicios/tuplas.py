#Tuplas

"""
Crear una tupla con números, luego pedir un número por teclado e indicar cuántas veces se repite
"""

numeros = (5,6,6,7,8,8,10,12,8)

numero = int(input("Dame un número: "))

print("El número se repite: " + str(numeros.count(numero)) + " veces.")


print("El número " + str(numero) + " se encuentra en el índice: " + str(numeros.index(numero)))

