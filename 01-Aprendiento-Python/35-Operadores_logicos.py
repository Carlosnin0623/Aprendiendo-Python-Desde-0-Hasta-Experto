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
