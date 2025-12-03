# Condicional if anidado

edad = int(input("Digite su edad: "))
graduación = input("¿Ya te has graduado? (si) o (no): ")

if edad > 18:
    print("¡Felicidades! Ya tienes la mayoría de edad!")
    if graduación == "si":
        print("¡Felicidades por tu graduación!")


# otro ejemplo:

password = input("Ingrese su password: ")

if len(password) >= 8:
    print("Muy bien, contraseña suficientemente larga")

    if (password == "Prueba12345"):
        print("Además, es la contraseña correcta")
    else:
        print("Pero es incorrecta")
else:
    print("Tu contraseña es incorrecta e insegura")






