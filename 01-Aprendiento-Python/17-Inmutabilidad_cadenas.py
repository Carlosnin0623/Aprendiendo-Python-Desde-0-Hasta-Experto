"""
En python no podemos cambiar los valores de una cadena una vez ya definida, 
porque se protege

ejemplo:

texto = "Gato"

texto[0] = "p" Resultado: TypeError: 'str' object does not support item
assignment.

Lo que podemos hacer es concatenarle otras palabras para que asi el texto 
pueda ser modificado

"""

animal = "Gato"

# animal[4] = "s" Provoca un error

# CORRECTO: concatenar (Sumar)

# Tomamos "Gato" + "s" y lo guardamos en una nueva variable
plural = animal + "s"

print(animal) #Salida: "Gato" Intacto
print(plural) #Salida: "Gatos" (Nuevo Objeto)

# Concatenacion con f-strings
plural = f"{animal}s"
print(plural)