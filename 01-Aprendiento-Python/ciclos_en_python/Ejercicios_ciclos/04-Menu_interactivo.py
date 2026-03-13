"""
Crear un menú interactivo para el usuario
"""

print('*** Sistema de Administración de Cuentas ***')

salir = False

while not salir:
    print(f'''
    1. Crear Cuenta
    2. Eliminar Cuenta
    3. Salir
    ''')
    opcion = int(input('Escoje una opción:'))
    if opcion == 1:
        print('Creando cuenta...\n')
    elif opcion == 2:
        print('Eliminando cuenta...\n')
    elif opcion == 3:
        print('Saliendo del programa...')
        salir = True