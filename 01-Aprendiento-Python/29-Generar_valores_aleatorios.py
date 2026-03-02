"""
Generar valores aleatorios

La función randint(), que parte de un modulo llamado 'random', nos permite
generar números aleatorios

randint(a,b) devuelve un número aleatorio entre a y b, incluyendo esto valores.


Es necesario importar en primer lugar el modulo de random antes de usar
la funcion randint.

Para importar un modulo, usamos la sintaxis siguiente:

Import random
"""

from random import randint

# Generar un numero entre 1 y 10
numero = randint(1, 10)

print(f"Número aleatorio entre 1 y 10: {numero}")


#2. Simular un dado de 6 caras

dado = randint(1,6)
print(f"El número del dado es: {dado}")