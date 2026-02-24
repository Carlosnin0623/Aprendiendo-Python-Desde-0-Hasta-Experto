"""
¿Que es el Slicing?

Imagina que un texto es como una barra de pan cortada en rebanadas

El Slicing: Es la técnica para extraer un fragmento especifico sin 
modificar el orginal.

Indices Positivos
 0   1   2   3   4   5   6   7   8   9  10  11

"P" "R" "O" "G" "R" "A" "M" "A" "C" "I" "O" "N"

Indices negativos
-12 -11 -10 -9  -8  -7  -6  -5  -4  -3  -2  -1
"""

texto = "PROGRAMACION"

# 1.Basico [inicio:fin]
print(texto[0:4]) # Resultado: PROG (El índice final no se incluye ya que se aplica un -1)


# 2.Atajo desde el inicio [:fin]

print(texto[:4]) # Resultado: PROG (El índice final no se incluye ya que se aplica un -1)


# 3.Atajo hasta el final [inicio:]

print(texto[8:]) #Resultado: CION (Cuenta desde el indice seleccionado hasta el final)


# 4. Indices Negativos

print(texto[-4:]) # Resultado: CION 

# 5. Retornar cadena invertida para esto dejamos el indice de inicio
# vacio usando :, tambien dejamos el indice de fin vacio usando :, y luego el indice de paso
# Esto lo que hacemos es recorrer cada uno de los elementos. con el -1 retornamos la cadena invertida.

print(texto[::-1]) #Resultado: NOICAMARGORP es PROGRAMACION alrevés

# 6. Tambien podemos indicarle que haga saltos de 2 en 2, con indices negativos

print(texto[::-2]) # Resultado: NIAAGR

# 7. Tambien podemos indicarle que haga saltos de 2 en 2, con indices positivos

print(texto[::2]) # Resultado: PORMCO





