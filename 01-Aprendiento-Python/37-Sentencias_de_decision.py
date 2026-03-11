"""
Las sentencias de decisión nos permiten controlar el flujo de ejecución de
un programa.

Las estrucuras que podemos usar son: if, else y elif

La sentencia if permite ejectutar un bloque de codigo si la condicion a evaluar
es verdadera. Una condición es una expresion que evalua True o False.

Sintaxis:

if condición:
  # Bloque de codigo que se ejecuta si la condición es True.

Ejemplo sentencia if
 edad = 30

if edad >= 30:
  print('Eres mayor de edad')
"""

# Sentencia if

edad = 30

if edad >= 30:
    print(f'Eres mayor de edad tienes: {edad}') 


# Sentencia if else

"""
Sentencia if else

La sentencia else se usa para ejecutar un bloque de codigo cuando la condicion
del if es falsa

# sintaxis sentencia if else 

if condición:
  # Bloque de codigo que se ejecuta si la condicion es verdadera.
else:
  # Bloque de condición que se ejecuta si la condición es falsa.
"""

edad = 28

if edad >= 30:
    print(f'Eres mayor de edad, tienes: {edad} años de edad')
else:
    print(f'No eres mayor de edad, tienes {edad} años de edad')


"""

Sentencia if elif else

La sentencia elif es una abreviatura de "else if " y se utiliza cuando
necesitamos verificar multiples condiciones, una tras otra.

Se pueden agregar tantas nuevas condiciones de tipo elif como necesitemos
, pero deben ir despues de un if y antes del bloque else

sintaxis sentencia if else

if condicion:
  # Bloque de codigo condicion1 True
elif condicion2:
  # Bloque de codigo condicion2 True
else:
  # Bloque de codigo cuando ninguna de las condiciones anteriores fue verdadera
"""

#ejemplo elif

edad = 17

if (edad >= 18):
    print(f'Eres mayor de edad, tienes {edad}')
elif (edad >= 13 and edad < 18):
    print('Eres adolecente')
else:
    print('Eres un niño')