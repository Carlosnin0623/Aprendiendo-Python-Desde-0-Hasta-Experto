"""
Identifica la estación del año

Se solicita proporcionar el valor de un mes (valor numérico entre
1 y 12), e indicar la estación del año segun lo siguiente:

Meses 1,2 o 12  -> Invierno

Meses 3,4 o 5 -> Primera

Meses 6,7, o 8 -> Verano

Meses 9,10 o 11 -> Otoño

Cualquier otro valor -> Estación Desconocida
"""

import re

try:
   mes = input('Ingresa el mes y te dire a que estación del año pertenece: ')

    # validando que el usuario no pueda ingresar textos solo números
   if(not re.fullmatch(r'\d+', mes)):
    raise ValueError('No se permite introducir texto')
      
   mes = int(mes)
   if (mes not in [1,2,3,4,5,6,7,8,9,10,11,12]):
    raise ValueError ('Estación desconocida')
   
   if(mes in [1,2,12]):
     print('Invierno')
   elif(mes in [3,4,5]):
     print('Primavera')
   elif(mes in [6,7,8]):
     print('Verano')
   else:
     print('Otoño')

except ValueError as e:
   print(f'Ocurrio un error ->: {e}')



