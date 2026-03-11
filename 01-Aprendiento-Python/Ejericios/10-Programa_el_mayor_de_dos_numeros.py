"""
El mayor de 2 números

Crear un programa para indicar cual es el mayor de dos números.

El programa debe pedir al usuario dos números enteros.

Posteriormente se deben comparar y mandar a imprimir el número mayor
"""
import re # Este modulo es util para crear expresiones regulares y sirve para validar entradas de datos

try:

 print('\n*** Este programa mostrara el numero mayor entre 2 números ***')

 primer_numero = input('Ingresa el primer número:')

 """
   Explicación rápida

   \d → significa dígito (0-9)

    + → significa uno o más

    re.fullmatch() → asegura que toda la cadena sea números
 """
 if not re.fullmatch(r'\d+', primer_numero):
    raise ValueError('Lo sentimos, no se permite ingresar letras ni números negativos en este campo')
 
 segundo_numero = input('Ingresa el segundo número:')

 """
   Explicación rápida

   \d → significa dígito (0-9)

    + → significa uno o más

    re.fullmatch() → asegura que toda la cadena sea números
 """
 if not re.fullmatch(r'\d+', segundo_numero):
    raise ValueError('Lo sentimos, no se permite ingresar letras ni números negativos en este campo')
 
 primer_numero = int(primer_numero)
 segundo_numero = int(segundo_numero)

 if primer_numero > segundo_numero:
   print('El primer número es mayor que el segundo número')
 elif segundo_numero > primer_numero:
   print('El segundo número es mayor que el primer número')
 elif segundo_numero == primer_numero:
   print('Los números son iguales')
 else:
   print('Los números son iguales')
 
except ValueError as e:
 print(f'Ha ocurrido un error! -> {e}')
finally:
  print('Flujo terminado')