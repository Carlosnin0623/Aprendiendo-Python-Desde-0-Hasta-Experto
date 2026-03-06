"""
Operadores Lógicos

Los operadores lógicos se utilizan para realizar operaciones lógicas con valores booleanos.

Operador Lógico and (y): Devuelve True si ambos operandos son verdaderos.

Operador Lógico or (o): Devuelve True si cualquiera de los operandos es verdadero.

Operador Lógico not (no): Invierte el valor del operando. Es un operador unario.

"""

print("*** Operador and ***")

# Regresa verdadero si ambos valores a evaluar son verdaderos
condicion1 = False
condicion2 = False
resultado = (condicion1 and condicion2)
print(f'El resultado {condicion1} and {condicion2}: {resultado}')


print("*** Operador or ***")

# El operador or regresa True si cualquiera de los operandos es True
condicion1 = False
condicion2 = False
resultado = (condicion1 or condicion2)
print(f'El resultado {condicion1} and {condicion2}: {resultado}')


print("*** Operador not ***")

condicion1 = False
resultado = not condicion1 # El operador not invierte el valor del operando
print(f'Operador not sobre {condicion1}: {resultado}')

# Revisar si una variable es cadena vacia
nombre = 'Juan'
es_cadena_vacia = not nombre
print(f'\nLa variable no tiene ningún valor? {es_cadena_vacia} ')

# Revisar si una variable no tiene ningún valor asignado

variable = None
es_variable_sin_valor = not variable
print(f'\nLa variable No tiene ningún valor asignador? {es_variable_sin_valor}')