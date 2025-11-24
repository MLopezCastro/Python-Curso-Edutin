# Ciclo for

word = input("Ingrese una palabra: ")

for i in range(3):
    print(word)


print("Comienzo")
for i in [3,4,5,6]:
    print(f"Ahora i vale {i} y su cuadrado vale {i**2}")
print("Final")



print("Comienzo")
contador = 1
for i in [3,4,5,6]:
    print(f"Vuelta número: {contador}")
    print(f"Hola, ahora i vale {i} y su cuadrado vale {i**2} ")
    contador += 1
print("Final")