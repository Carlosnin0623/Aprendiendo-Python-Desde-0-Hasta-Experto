"""
Los operadores de comparación se utilizan para comparar 2 valores, el resultado
siempre es un valor booleano 'True' o 'False' dependiendo de que si la 
condición se cumple o no.

"""

# Operador de igualdad (==): Compara si dos valores son iguales
print(5 == 5) # True
print(5 == 6) # False

# Operador de distinto !=: Compara si dos valores son distintos.
print(5 != 5) # False
print(5 != 6) # True

# Operador menor que (<): Compara si el valor de la izquierda es menor que el de la derecha

print(5 < 6) # True
print(5 < 3) # False

# Operador menor o igual que (<=): Compara si el valor de la izquierda es menor o igual al de la derecha

print(5 <= 6) # True
print(5 <= 3) # False

# Operador mayor que (>): Compara si el valor de la izquierda es mayor que el de la derecha

print(5 > 6) # False
print(5 > 3) # True

# Operador mayor o igual que (>=): Compara si el valor de la izquierda es mayor o igual al de la derecha

print(5 >= 6) # False
print(5 >= 3) # True
print(5 >= 5) # True


print("*** Operadores Comparación (Relacionales) ***")

"""
Los operadores de comparación relacionales

Los operadores de comparación relacionales se utilizan para comparar 2 valores, el resultado
siempre es un valor booleano 'True' o 'False' dependiendo de que si la 
condición se cumple o no.

"""

a,b = 5,5
print(f'Valor inicial a: {a}, b {b}')

# Operador igualdad == 
resultado = (a == b)
print(f'Resultado a == b: {resultado}')

# Operador diferente !=
resultado = (a != b)
print(f'Resultado a != b: {resultado}')

# Operador mayor que >
resultado = a > b
print(f'Resultado a > b: {resultado}')

# Operador mayor o igual que >= 
resultado = a >= b
print(f'Resultado a >= b: {resultado}')
