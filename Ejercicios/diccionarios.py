#Primera forma de crear un diccionario
diccionario = {
    "nombre":"Mario",
    "edad":20,
    "documento": 545220
}
print(diccionario)



#Segunda forma de crear un diccionario
diccionario_segunda_forma = dict(Nombre="Mario",
                                 edad=20,
                                 documento=545220)
print(diccionario_segunda_forma)



#Tercera forma de crear un diccionario
diccionario_tercera_forma = dict([
    ("nombre","Mario"),
    ("edad",20),
    ("documento",545220)
])
print(diccionario_tercera_forma)



#Ejercicio:
inventario = {"Manzanas":50,"Naranjas":30,"Peras":45}
print(inventario)
print(inventario.items())
print(inventario.keys())
print(inventario.values())

