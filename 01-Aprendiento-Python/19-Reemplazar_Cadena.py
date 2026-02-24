"""
¿Qué es replace?

1- (Buscar): Encuentra todas las coincidencias de un texto.
2- (Sustituir): Sustituir lo viejo por lo nuevo automaticamente.
3- (Copia Nueva): No modifica el original, crea uno nuevo.
4- (Limpieza): Eliminar especios extra, símbolos raros o erroes.
5- (Plantilla): Cambiar "{nombre}" por el nombre real del usuario.

Sintaxis
texto.replace("viejo","nuevo")

Toma dos argumentos obligatorios: que buscar y que poner
en su lugar.

.replace("viejo","nuevo",2)
opcional:Agrega un número al final para limitar cuántos cambiar.

"""

# Programa: Reemplazar textos en python

mensaje = "Hola Mundo, Mundo"

# Reemplazar todas las apariciones

nuevo = mensaje.replace("Mundo", "Python") # Salida: "Hola Python, Python"

# Reemplazar solo una vez, remplza solo la primera aparicion de la palabra
uno_solo = mensaje.replace("Mundo", "Dev", 1) # Salida: "Hola Dev, Mundo"