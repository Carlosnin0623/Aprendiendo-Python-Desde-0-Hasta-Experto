"""
Realizar la suma de los primeros 5 números utilizando un ciclo while

"""

import time

contador = 1
resultado = 0

while contador <= 5:
    print(f"\n(acumulador_suma + numero) -> {resultado} + {contador}")
    resultado += contador
    print(f'Suma parcial acumulada: {resultado}')
    contador += 1
    time.sleep(2)
