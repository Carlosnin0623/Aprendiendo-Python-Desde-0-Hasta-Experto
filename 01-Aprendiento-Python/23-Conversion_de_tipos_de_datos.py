"""
¿Qué es el casting?

Es el proceso de transformar un dato de un tipo a otro.

Texto -> Número

En python tenemos 3 funciones claces para la transormación explícita.

int(): Convierte texto o decimales a Enteros.
float(): Convierte texto o enteros a decimales.
str(): Convierte cualquier cosa a Texto.
"""

# Programa: Convertir tipos en Python

# Definimos una variable de tipo string

numero_texto = "50"

total = int(numero_texto)  + 10

print(f"El total es: {total}") # Resultado: 60

concatenacion = numero_texto + str(10)

print(f"El resultado de la concatenación es: {concatenacion}") # Resultado: 5010

