"""
Programa que simula un cajero automático
"""

import re
import time

salir = False
saldo_actual = 1000.00

while not salir:
    try:
        print("""
        ===============================
        Aplicación de Cajero Automático
        ===============================
        Menú:
        1. Consultar Saldo
        2. Retirar
        3. Depositar
        4. Salir
        """)

        opcion = input('Escoge una opción: ').strip()

        # Validar que solo sean números
        if not re.fullmatch(r'\d+', opcion):
            raise ValueError('Debes ingresar solo números del menú.')

        opcion = int(opcion)

        if opcion not in [1, 2, 3, 4]:
            raise ValueError('La opción elegida no es válida.')

        # CONSULTAR SALDO
        if opcion == 1:
            print(f'\nTu saldo actual es: RD${saldo_actual:.2f}')

        # RETIRAR
        elif opcion == 2:
            retirar = input('Ingrese la cantidad a retirar: ').strip()

            if not re.fullmatch(r'\d+(\.\d+)?', retirar):
                raise ValueError('Debes ingresar un número válido.')

            retirar = float(retirar)

            if retirar <= 0:
                raise ValueError('El monto debe ser mayor que 0.')

            if saldo_actual == 0:
                print('Tu cuenta no tiene fondos disponibles.')

            elif retirar > saldo_actual:
                print(f'Fondos insuficientes. Tu saldo es RD${saldo_actual:.2f}')

            else:
                saldo_anterior = saldo_actual
                saldo_actual -= retirar
                print(f'''
                Retiro realizado correctamente
                Saldo anterior: RD${saldo_anterior:.2f}
                Monto retirado: RD${retirar:.2f}
                Saldo actual: RD${saldo_actual:.2f}
                ''')

        # DEPOSITAR
        elif opcion == 3:
            depositar = input('Ingrese la cantidad a depositar: ').strip()

            if not re.fullmatch(r'\d+(\.\d+)?', depositar):
                raise ValueError('Debes ingresar un número válido.')

            depositar = float(depositar)

            if depositar <= 0:
                raise ValueError('El monto debe ser mayor que 0.')

            saldo_anterior = saldo_actual
            saldo_actual += depositar

            print(f'''
            Depósito realizado correctamente
            Saldo anterior: RD${saldo_anterior:.2f}
            Monto depositado: RD${depositar:.2f}
            Saldo actual: RD${saldo_actual:.2f}
            ''')

        # SALIR
        elif opcion == 4:
            print('Saliendo del sistema...')
            time.sleep(2)
            print('Gracias por usar el cajero automático.')
            salir = True

    except ValueError as e:
        print(f'\nError: {e}\n')