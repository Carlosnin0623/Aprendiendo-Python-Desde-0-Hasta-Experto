"""
Operadores de Asignacion Compuestos:

Los operdores de asignacion compuestos combinan una operación aritmetica con una asignación, haciendo las operaciones
mas consisas.

Los operadores puede ser +=, -=, *=, /=, etc

"""

# Ejemplo operador de asignacion compuesto
contador = 0
contador += 1 # contador = contador + 1

print("\n *** Operadores de Asignacion compuesto  *** \n")

a,b = 10, 15
print(f"El valor inicial a: {a}, b: {b}")

# Operador compuesto de suma +=
a += b # a = a + b
print(f'Operador a += b es: {a}')

# Operador compuesto de resta -=

a = 10# reiniciamos la variable a
a -= b # a = a - b
print(f'Operador a -= b es: {a}')

# Operador compuesto de multiplicación *=

a = 10 # Reiniciamos el valor
a *= b
print(f'Operador a *= b es: {a}')

# operador compuesto de división /=
a = 10
a /= b
print(f'Operador a /= b es: {a:.2f}')

# Operador compuesto division entera //=
a = 10
a //= b
print(f'Operador a //= b es: {a}')

# Operador compuesto módulo o residuo
a = 10
a %= b
print(f'Operador a %= b es: {a}')

# Operador compuesto potencia **=
a = 10
a **= b
print(f'Operador a **= b es: {a}')