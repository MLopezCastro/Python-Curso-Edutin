# actividad_condicionales

# Solicitar información:

nombre = input("Ingrese el nombre del cliente: ")
valor_compra = int(input("Ingrese el valor de compra: "))

# Establecer condiciones:

if valor_compra < 80:
    descuento = 0
    print(f"Hola, {nombre}, el valor a pagar es: ${valor_compra}")
elif 80 <= valor_compra <= 150:
    descuento = 0.1
elif 150 <= valor_compra <= 300:
    descuento = 0.15
elif 300 <= valor_compra < 500:
    descuento = 0.2
else:
    descuento = 0.3

monto_descuento = valor_compra * descuento
precio_final = valor_compra - monto_descuento


print(f"Hola, {nombre}, el valor original -compra sin descuento- es ${valor_compra}")
print(f"El descuento es de: {descuento}")
print(f"El precio final es de: {precio_final}")

"""
Angel Mario Villa Lopez realizó una compra de 455 usd: Valor: $ 364.0

Rosa Diaz realizó una compra de 105 usd: Valor: $ 94.5

Dilan Gonzalez realizó una compra de 250 usd: Valor: $212.15

Kelly Daza realizó una compra de 430 usd: Valor: $ 344.0
"""