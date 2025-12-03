"""
Escribir un programa que almacene las asignaturas de un curso
"""
asignaturas = ["Matemáticas","Física","Español","Inglés"]

print(type(asignaturas))
print(asignaturas[0])
print(asignaturas[1])
print(asignaturas[2])


#Lotería
numeros = []
for i in range(6):
    numeros.append(int(input(f"Introduce un numero: ")))

numeros.sort()
print(f"Los números ganadores son: {numeros}")


#Otro ejemplo:

lista = [1,4,5,7,9]
for i in lista:
    print(i)

#Otro ejemplo:
lista = [1,4,5,7,9,"Hola"]
for i in lista:
    print(i)

lista.remove(4)
lista.pop(3)
del lista[0]
lista.clear() #vacía la lista
print("Esta es la lista después de colocar el método clear")
for i in lista:
    print(i)




