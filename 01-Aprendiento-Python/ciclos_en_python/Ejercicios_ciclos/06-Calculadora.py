"""
Aplicación Calculadora

Crear una aplicación de calculadora con las opciones de:

1. Suma
2. Resta
3. Multiplicación
4. División


El programa debe mostrar un menú con cada opción, y debe solicitar los valores de operando 1 y operando 2
para realizar la operacion seleccionada.

"""

import re, time

salir = False

num1 = 0.00
num2 = 0.00
resultado = 0.00

while not salir:
   try:
    print(f'''
     *** Calculadora en Python ***
     Operaciones que puedes realizar:
     Menú:
     1. Suma
     2. Resta
     3. Multiplicación
     4. División
     5. Salir
     ''')
    opcion = input('Escoge una opción:')

    if(not re.fullmatch(r'\d+',opcion)):
      raise ValueError('Solo puedes introducir números')
    
    opcion = int(opcion)
    if(opcion not in [1,2,3,4,5]):
      raise ValueError('La opción elegida no es valida...,escoja una de las opciones del menú')
    
    if(opcion == 1):
      num1 = input('Escribe el primer número:')
      if(not re.fullmatch(r'\d+(\.\d+)?',num1)):
       raise ValueError('Solo puedes introducir números')
      
      num2 = input('Escribe el segundo número:')
      if(not re.fullmatch(r'\d+(\.\d+)?',num2)):
       raise ValueError('Solo puedes introducir números')
      
      num1 = float(num1)
      num2 = float(num2)
      resultado = num1 + num2
      print(f'El resultado es: {resultado:.2f}')

    if(opcion == 2):
      num1 = input('Escribe el primer número:')
      if(not re.fullmatch(r'\d+(\.\d+)?',num1)):
       raise ValueError('Solo puedes introducir números')
      
      num1 = float(num1)
      
      num2 = input('Escribe el segundo número:')
      if(not re.fullmatch(r'\d+(\.\d+)?',num2)):
       raise ValueError('Solo puedes introducir números')
      
      num2 = float(num2)
      
      resultado = num1 - num2
      print(f'El resultado es: {resultado:.2f}')

    if(opcion == 3):
      num1 = input('Escribe el primer número:')
      if(not re.fullmatch(r'\d+(\.\d+)?',num1)):
       raise ValueError('Solo puedes introducir números')
      
      num1 = float(num1)
      
      num2 = input('Escribe el segundo número:')
      if(not re.fullmatch(r'\d+(\.\d+)?',num2)):
       raise ValueError('Solo puedes introducir números')
      
      num2 = float(num2)
      
      resultado = num1 * num2
      print(f'El resultado es: {resultado:.2f}')

    if(opcion == 4):
      num1 = input('Escribe el primer número:')
      if(not re.fullmatch(r'\d+(\.\d+)?',num1)):
       raise ValueError('Solo puedes introducir números')
      
      num1 = float(num1)
      
      num2 = input('Escribe el segundo número:')
      if(not re.fullmatch(r'\d+(\.\d+)?',num2)):
       raise ValueError('Solo puedes introducir números')
      
      num2 = float(num2)

      if(num2 == 0):
        raise ValueError('No puedes dividir por 0')
      
      resultado = num1 / num2
      print(f'El resultado es: {resultado:.2f}')

    if(opcion == 5):
      print('Cerrando calculadora...')
      time.sleep(2)
      salir = True
      
   except ValueError as e:
     print(f'Ha ocurrido un error: {e}')