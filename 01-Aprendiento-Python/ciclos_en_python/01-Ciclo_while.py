"""
Los ciclos en python son estructuras de control que repiten un serie de instrucciones hasta que se cumple 
una condición específica.

En Python tenemos dos tipos de estructuras para ejecutar ciclos Ciclo while y Ciclo For, Comencemos con el ciclo
while.

El ciclo While repite una serie de instrucciones miemras la condición a evaluar sea verdadera.

# Sintaxis ciclo while
 
while condicion:
  # Bloque de código a ejecutar
"""

# ejemplo1: Imprimir del 1 al 3

contador = 1

while contador <= 5:
    """
     Funcion Print en ciclos While y for

     Por defecto la funcion print, muestra los valores seprados en una filas diferente pero si queremos
     que en un bucle salga todo en una misma fila, la funcion print tiene un segundo parámetro llamado
     end = '' y aqui le especificamos como terminara cada linea, si lo dejamos vacio imprimira todo en la misma linea, pero
     si en el paramtreo end= le agregamos '\n' entonces hara un salto de linea cada vez que imprima esto es en el caso
     de los bucles
    """
    print(contador, end='\n') # 
    contador += 1


