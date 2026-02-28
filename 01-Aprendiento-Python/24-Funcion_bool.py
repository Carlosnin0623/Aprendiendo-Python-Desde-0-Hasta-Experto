"""
La función bool(): Es el mecanismo de Python para determinar la "existencia" o el "Vacio" de un dato.

Falsy:

Representan "Nada" o "Vacio".

0   (Cero int/float)
" " (String Vacío)
[] (Lista vacía)
None (Ausencia de valor)

Truthy

Cualquier cosa que "Existe".

1, -5, 3.14 (No cero)
"Hola", " " (Espacio)
[0] (Lista con datos)
True
"""

# Programa: Función bool

# 1. Números (int y float)

print(bool(0))  #False (El vacío numérico)
print(bool(0.0)) #False
print(bool(42)) # True (Existe valor)

# 2. Texto (Strings)
# Cadena vacía = Nada = False
print(bool("")) #False

# Cadena con espacio o texto = Algo = True
print(bool(" ")) # True
print(bool("Hola")) # True

# 3. None (Ausencia Total)
vacio = None
print(bool(vacio)) # False

print(bool(False)) # False
print(bool(True)) # True

