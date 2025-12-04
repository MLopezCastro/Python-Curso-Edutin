#Conjuntos

#Primera forma de crear conjuntos:

alumnos = {"Marcelo", "John", "Beto", "Goku"}

print(alumnos) #{'Goku', 'Beto', 'Marcelo', 'John'} no respeta orden



#Segunda forma de crear conjuntos:

lenguajes = set(["SQL", "Python", "PBI", "Excel"])

print(lenguajes) # {'Excel', 'PBI', 'SQL', 'Python'}

#lenguajes.add:
lenguajes.add("Github")
print(lenguajes)

#lenguajes.pop() Elimina un elemento
lenguajes.pop()
print(lenguajes)

#Para unir conjuntos:

todos = alumnos.union(lenguajes)
print(todos)
