"""

Subcadenas en Python

Buscar subcadenas (find): El método find devuelve el índice de la primera
aparición de la subcadena. Si no encuentra la subcadena, devuelve -1


 cadena = "Hola mundo"
 posicion = cadena.find("mundo")
 print(posicion)

"""

# Buscar subcadenas

cadena = "Hola mi querido mundo, en Python"

# si existe la cadena, devolverá el índice de la primera palabra del texto a buscar
indice = cadena.find("mundo")

# identificando una cadena si existe en cualquier texto

resultado = cadena[indice:indice + 5] 
print(resultado) # Resultado: mundo