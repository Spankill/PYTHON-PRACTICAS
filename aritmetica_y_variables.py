print("Hola mundillo")


print(1+2)   #suma

print(9-5)  #resta

print(5*4)  #multipl    

print(50/2) #divison

print(3**2) #elevado a..

print(((1 + 3) * (9 - 2) / 2) ** 2)   # operacion con parentesis operacioens agrupadas

#variables

variable=5+2
print(variable)


mi_variable = 6
print(mi_variable)

mi_variable = 22
print(mi_variable)

print(variable)
print(mi_variable)

#creamos variables

num_anios=5
dias_por_anio=365
horas_por_dia=24
minutos_por_hora=60
segundos_por_minuto=60

#calculamos el total de segundos en 5 anios

totalSegundos = segundos_por_minuto * minutos_por_hora * horas_por_dia * dias_por_anio * num_anios
print(totalSegundos) 

# resultado : 126144000

#calculando anios bisiestos
dias_por_anio = 365.25

#calculando total de segundos en 5 anios

totalSegundos = segundos_por_minuto * minutos_por_hora * horas_por_dia * dias_por_anio * num_anios
print(totalSegundos)

print(segundos_por_minuto)


#calcular el numer ode nacimientos de cada dia
births_per_min = 250
hours_per_day = 24
mins_per_hour = 60

births_per_day = births_per_min * mins_per_hour * hours_per_day 
print(births_per_day)


#cadenas
mi_string = "cadenita de texto"
mi_string = "nuevo texto"
print(type(mi_string))
print(mi_string)

mi_string = 6
print(type(mi_string))
print(mi_string)

mi_entero = 5
mi_entero = (mi_entero + 5)

print(mi_entero)


mi_flotante = 5.15
mi_flotante = (mi_flotante + 3.5)

print(mi_flotante)


mi_booleano = True
mi_booleano = False
print(type(mi_booleano))
print(mi_booleano)

print("el valor de mi entero es " + str(mi_entero) + "y el de mi_booleano " + str(mi_booleano))
print(f"el valor de mi entero es {mi_entero} y el de mi booleano es {mi_booleano}")

mi_lista = [mi_string, mi_entero, mi_flotante, mi_booleano]
print(type(mi_lista))
mi_lista.append(mi_booleano)
print(mi_lista)
print(mi_lista[0])