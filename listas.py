# listas


mi_lista = list()
mi_otra_lista =[]

print(len(mi_lista))

mi_lista = [99,85,62,41,75,63,2,56,8,96]

print(mi_lista)
print(len(mi_lista))

mi_otra_lista = [53,1.79, "Vizkcha87", "aruhiza"]

print(type(mi_lista))
print(type(mi_otra_lista))

#Busqueda y acceso a elementos

print(mi_otra_lista[0])
print(mi_otra_lista[1])
print(mi_otra_lista[-2])
print(mi_otra_lista[-4])
print(mi_lista.count(56))
#print(mi_otra_lista[4]) IndexError
#print(mi_otra_lista[-5]) IndexError

print (mi_otra_lista.index("Vizkcha87"))

age,height, name,subname = mi_otra_lista
print(name)

name,height,age,subname = mi_otra_lista[2], mi_otra_lista[1], mi_otra_lista[0],mi_otra_lista[3]
print(age)

#concatenacion

print(mi_lista + mi_otra_lista)
#print(mi_lista - mi_otra_lista) 

#Creacion Insercion Actualizacion y eliminacion de elementos en listas

mi_otra_lista.append("Vizkcha87")
print(mi_otra_lista)

mi_otra_lista.insert(2, "Aruhiza")
print(mi_otra_lista)

mi_otra_lista[1] = "Celeste"
print(mi_otra_lista)

mi_otra_lista.remove("Aruhiza")
print(mi_otra_lista)

print(mi_lista.pop())
print(mi_lista)

mi_pop_element = mi_lista.pop(2)
print(mi_pop_element)
print(mi_lista)


# Operando listas

mi_nueva_lista = mi_lista.copy()
mi_lista.clear()
print(mi_lista)
print(mi_nueva_lista)

mi_nueva_lista.reverse()
print(mi_nueva_lista)

mi_nueva_lista.sort()
print(mi_nueva_lista)

mi_nueva_lista.sort()
print(mi_nueva_lista)

