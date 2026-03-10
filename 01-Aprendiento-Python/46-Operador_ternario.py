"""
Operador Ternario

El operador ternario en Python es una forma compacta de agregar una condición, y el objetivo es asignar una 
valor a una variable dependiendo del valor de la condición.

# Sintaxis Operador Ternario
resultado = valor si es verderdo if condicion else valor si es falso.

# Ejemplo Operador Ternario
edad = 18
es_adulto = "Sí" if edad >= 18 else "No"
print(es_adulto)
"""

edad = int(input('Indica cual es tu edad?:'))
es_adulto = "Ya eres mayor de edad" if edad >= 18 else "Todavía eres menor de edad"
print(es_adulto)

