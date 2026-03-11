"""
Sistema Bancario

Considerando que estamos dentro de un sistema bancario, se solicita preguntar al usuario si desea
continuar dentro del sistema.


Utilizando el operador not para aplicar una lógica inversa se debe programar las siguiente condiciones:

Si no deseamos salir del sistema, imprimir:
   Continuamos dentro del sistema...
De lo contrario, imprimimos:
   saliendo del sistema...
"""

salir_sistema_txt = input('Desea permanecer en el sistema: Si / No?: ')
salir_sistema = salir_sistema_txt.strip().lower() == 'si'

if not salir_sistema:
    print('Continuamos dentro del sistema')
else:
    print('Salimos del sistema')