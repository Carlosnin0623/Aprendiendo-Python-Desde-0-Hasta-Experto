"""
Operadores en Python

Los operadores son símbolos especiales que están diseñados para realizar operaciones  
específicas. Tenemos varios tipos, como son:

Operadores Aritméticos: Permiten realizar cálculos matemáticos basicos, como suma,
resta, multiplicación o división.

Operadores de Asignación: Se utilizan para asignar valores a variables.

Operadores de comparación: Se utiliza para comparar un valor con otro.

Operadores lógicos: Se utilizan para combinar expresiones condicionales o lógicas.

Operadores de identidad: Se utilizan para comparar si dos variables son el mismo objeto.

Operadores de membresía: Se utilizan para probar si una secuencia Ej: (Una subcadena) se presenta 
como un objeto.
"""

# Operadores Aritmeticos
print("\n*** Operadores Aritméticos ***")
a = 10
b = 3

# Suma
suma = a + b
print(f'Suma: {suma}')

# Resta -
resta = a - b
print(f'Resta: {resta}')

# Multiplicación *
multiplicacion = a * b
print(f'Multiplicación: {multiplicacion}')

# División
division = a / b # Retorna un tipo flotante
print(f'División: {division}')

# Division Entera
division_entera = a // b # Retorna un int
print(f'División Entera: {division_entera}')

# Módulo (%) residuo de la division o resultado de la división
modulo = a % b
print(f'Residuo de la división: {modulo}')

# Exponente (Potencia) **
exponente = a ** b # 10 elevado a las 3 = 10*10*10=1000
print(f'Exponente: {exponente}')

# Operadores de Asignación

print("\n*** Operadores de Asignación ***")
numero = 5
print(f'Valor de numero: {numero}')

cadena = 'Saludos desde Python'
print(f'Valor de la cadena: {cadena}')

"""
Asignación multiple

En Python tambien tenemos la asignación múltiple. lo que nos permite asignar valores a varias variables en una sola
linea de código. El código es más compacto y facil de leer.
"""

# Sintaxis de Asignacion Múltiple
variable, variable2 = 10, 20

print(f'Valor de la primera variable: {variable}') # Resultado 10
print(f'Valor de la segunda variable {variable2}') # Resultado 20

"""
Asignación Encadenada

En Python tambien contamos con la asignación encadenada, 
esto permite asignar el mismo valor a multiples variables.

"""

# Ejemplo Inicializar contadores
contador1 = contador2 = 0

print(f"El valor del contador1 es: {contador1}") # Resultado: 0
print(f"El valor del contador2 es: {contador2}") # Resultado: 0

# Intercambio de valores de una variable, sin utilizar variables temporales
x,y = 5, 10
print(f'Valores iniciales x = {x}, y = {y}')
# Aplicando el concepto de asignacion multiple, intercambiamos valores.
x,y = y,x
print(f'Invertir los valores x = {x}, y = {y}')

# Recibir multiples valores de la entrada del usuario

nombre, apellido = input('Ingresa tu nombre y apellido separados por coma: ').split(',')
print(f'Nombre: {nombre.strip()}')
print(f'Apellido: {apellido.strip()}')


