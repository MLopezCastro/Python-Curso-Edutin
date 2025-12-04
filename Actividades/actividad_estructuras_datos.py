# Diccionario "agenda"

#Define el diccionario con el nombre “agenda” y añade los nombres y teléfonos:

agenda = {
    'Jose': 302944,
    'Mario': 829455,
    'Angel': 829405,
    'Luis': 930594,
}

# Define una variable con el nombre consultando e inicializarla con True,
# esta servirá para la condición del ciclo:

consultando = True

# Crea un menú sencillo utilizando el print(),
# además de otra variable con el nombre opción que por defecto estará vacía.

while consultando:
    print()
    print("MI AGENDA")
    print("-----------------")
    print("1. Consultar \n2. Añadir \n3. Modificar \n4. Borrar \n5. Salir")

    opcion = ""

# Define un ciclo while y compruebe si la persona ha seleccionado o no
# los números: 1, 2, 3, 4 y 5. En caso de que no lo haya hecho,
# muestre un input para que la persona elija la opción.

    while opcion not in ("1", "2", "3", "4"):
        opcion = input("->")

# Si la persona elige la primera opción, el programa deberá pedir el nombre
# y comprobar si está en el diccionario, en caso de que no esté se mostrará un mensaje de error,
# caso contrario se mostrará el número de teléfono asociado.

        if opcion == "1":
            # Pedir nombre
            nombre = input("Nombre: ")
            # Comprobar si el nombre está en el dicionario
            if nombre not in agenda:
                print("Este nombre no existe en la agenda")
            else:
                telefono = agenda[nombre]
                print(nombre, ":", telefono)

# Si la persona elige la segunda opción, el programa deberá pedir el nombre
# y comprobar si está en el diccionario, en caso de que se encuentre aparecerá un mensaje
# indicando que el nombre ya se encuentra, caso contrario pedirá el número de teléfono
# y lo guardará en la agenda.

        elif opcion == "2":
                # Pedir nombre
            nombre = input("Nombre: ")
                # Comprobar si el nombre está en el diccionario
            if nombre in agenda:
                print("Este nombre ya existe en la agenda")
            else:
                    # Añadir el telefono a la agenda:
                agenda[nombre] = telefono
                print("El teléfono se ha añadido correctamente")

# Si la persona elige la tercera opción, el programa deberá pedir el nombre
# y comprobar si está en el diccionario, en caso de que no se encuentre aparecerá un mensaje
# indicando que el nombre no existe en la agenda, caso contrario pedirá el nuevo número de teléfono,
# lo modificará y lo guardará en la agenda.

        elif opcion == "3":
                # Pedir nombre
            nombre = input("Nombre: ")
            if nombre not in agenda:
                print("Este nombre no existe en la agenda")
            else:
                telefono = int(input("Digite el telefono: "))
                    # Modificar el teléfono
                agenda[nombre] = telefono
                print("El teléfono se ha modificado correctamente")

# Si la persona elige la cuarta opción, el programa deberá pedir el nombre y
# comprobar si está en el diccionario, en caso de que no se encuentre aparecerá un mensaje
# indicando que el nombre no existe en la agenda, caso contrario borrará el número de teléfono
# de la agenda.

        elif opcion == "4":
                # Pedir nombre
            nombre = input("Nombre: ")
            if nombre not in agenda:
                    print("Este nombre no existe en la agenda")
            else:
                    # Borrar el teléfono
                del agenda[nombre]
                print("El telefono se ha borrado correctamente")

# Si la persona elige la quinta opción, simplemente cambiará la variable consultando de
# True a False y terminará de ejecutarse el ciclo.

        elif opcion == "5":
            consultando = False
            print("Gracias por utilizar el programa")



