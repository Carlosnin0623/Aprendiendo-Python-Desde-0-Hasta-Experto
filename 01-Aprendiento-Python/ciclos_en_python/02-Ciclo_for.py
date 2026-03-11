"""
Ciclo For en Python

EL ciclo for itera o recorre una secuencia de valores, por ejemplo los caracteres de una cadena, una lista
etc y ejecuta un bloque de código por cada elemento de la secuencia.

# Sintaxis ciclo for:
 for variable in secuencia:
   # bloque de codigo a ejecutar
"""

# Ejemplo Ciclo for
cadena = 'Hola mundo'

for letra in cadena:
    print(letra)

# Iterando sobre arreglos

frutas = ['Plátano', 'Fresa', 'Mango']

for fruta in frutas:
    print(fruta, end=' ')