"""
¿Para que sirve?

"Go" * 3 = "GoGoGo"

-- Separadores visuales

print("-" * 20) # resultado: --------------------


En python, el operador * crea copias concatenadas.

Formula

 "Cadena" * Entero

Por Cero o Negativo

"Text" * 0  Resultado: Cadena vacía "" (Desaparece)

Por Decimal (Float)

"Texto" * 3.5  Resultado: TypeError: Can't multiply sequence by non-int
"""

# Programa: Multiplicación de Cadenas

#1. Crear un seperador visual
linea = "=" * 20
print(linea)

#2. Identación simple
nivel = 2
sangria = "   " * nivel
print(sangria + "definición_bloque_codigo:")
