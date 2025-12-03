print("Bienvenido al conversor de monedas 🪙\n")

def conversor(moneda_actual, valor, moneda_a_convertir):

    # SUBFUNCIÓN PARA DÓLARES
    def dolarTo():
        if moneda_a_convertir == "1":
            print(f"{valor} dólares equivalen a {valor * 3750} pesos colombianos")
        elif moneda_a_convertir == "2":
            print(f"{valor} dólares equivalen a {valor * 6.37} yuanes")
        elif moneda_a_convertir == "3":
            print(f"{valor} dólares equivalen a {round(valor * 0.76, 2)} libras esterlinas")
        else:
            print("No se reconoce la moneda a convertir.")

    # SUBFUNCIÓN PARA EUROS
    def euroTo():
        if moneda_a_convertir == "1":
            print(f"{valor} euros equivalen a {valor * 4000} pesos colombianos")
        elif moneda_a_convertir == "2":
            print(f"{valor} euros equivalen a {valor * 6.93} yuanes")
        elif moneda_a_convertir == "3":
            print(f"{valor} euros equivalen a {round(valor * 0.83, 2)} libras esterlinas")
        else:
            print("No se reconoce la moneda a convertir.")


    # CONDICIONES PRINCIPALES APARTIR DE LA MONEDA ACTUAL
    if moneda_actual == "1":
        dolarTo()
    elif moneda_actual == "2":
        euroTo()
    else:
        print("Error: debe elegir 1 para dólares o 2 para euros.")


# ------------------ ENTRADAS DEL USUARIO ------------------ #

# 4. Moneda actual
moneda_actual = input("Seleccione moneda actual (1 = Dólar, 2 = Euro): ")

# 5. Valor a convertir
valor = float(input("Ingrese la cantidad a convertir: "))

# 6. Moneda destino
print("\nA qué moneda desea convertir:")
print("1. Pesos colombianos")
print("2. Yuanes")
print("3. Libras esterlinas")
moneda_a_convertir = input("Seleccione el número de opción: ")

# 7. Invocación de la función
conversor(moneda_actual, valor, moneda_a_convertir)


# 8. COMENTARIO MULTILÍNEA
"""
1. ¿Por qué usamos funciones?
   Para organizar el código, evitar repeticiones y mantener la lógica separada y clara.

2. ¿Qué ventajas tiene usar subfunciones?
   Permiten dividir tareas específicas (dólar y euro) y mantener el código más limpio.

3. ¿Qué pasaría si no usáramos condicionales?
   El programa no podría decidir qué conversión hacer, ni validar las opciones del usuario.
"""

