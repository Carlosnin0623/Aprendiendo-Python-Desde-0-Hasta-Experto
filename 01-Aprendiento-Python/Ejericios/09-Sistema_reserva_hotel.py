"""
Sistema Reserva Hotel

Se solicita crear un sistema de reservación de un hotel.
Se debe pedir la siguiente información al usuario:

- Nombre de Cliente
- Días de estadía en el Hotel.
- Cuarto con visita al mar?

El hotel tiene las siguientes tarifas:

 - Cuarto sin vista al mar: $150.50 por día
 - Cuarto con vista al mar: $190.50 por día

El sistema debe calcular el costo total de estadía dependiendo si escogió un cuarto con vista al mar o no.
Además de indicar si escogió un cuarto con vista al mar o no.
"""

costo_total = 0.0

try:
  nombre_cliente = input('Ingrese el nombre del cliente:').lower().strip()

  if not nombre_cliente:
    raise ValueError('el nombre del usuario no puede estar vacio')
  
  if nombre_cliente[0].isdigit():
    raise ValueError('el nombre del cliente no puede contener número al principio')
  
  dias_estadia = int(input('Ingrese los días de estadia:'))

  if dias_estadia < 0:
    raise ValueError('lo siento no es permitido agregar números negativos')
  
  if dias_estadia == 0:
    raise ValueError('debe agregar al menos 1 día de estadía')
  
  cuarto_con_vista_al_mar = input('Desea que su habitación tenga vista al mar (Si / No)?:').lower().strip()

  if any(char.isdigit() for char in cuarto_con_vista_al_mar):
    raise ValueError('no se permiten números en esta respuesta')

  if cuarto_con_vista_al_mar not in ['si', 'no']:
    raise ValueError('debe responder solamente "Si" o "No"')
  
  if not cuarto_con_vista_al_mar == 'si':
    costo_total = dias_estadia * 150.50
  else:
    costo_total = dias_estadia * 190.50
  print('\n*** Información de la reservación ***')
  print('_____________________________________\n')

  print(f'Nombre Cliente: {nombre_cliente}')
  print(f'Dias de estadía: {dias_estadia}')
  print(f'Tendra habitación con vista al mar?: {cuarto_con_vista_al_mar}')
  print(f'Costo total: US${costo_total:.2f} \n')

except ValueError as e:
  print(f'Ocurrió un error: {e}')
finally:
  print('Proceso terminado')
