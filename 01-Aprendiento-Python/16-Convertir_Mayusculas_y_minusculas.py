"""
Esto sirve para normalizar los datos que recibimos a traves de un formulario
como puede ser un correo electrónico o una entrada de datos.

upper: Permite convertir un texto de tipo string a mayúsculas.

lower: Permite convertir un texto de tipo string a minúsculas.
"""

mensaje = "Hola mi nombre es carlos"

palabra_mayuscula = mensaje.upper()

print(f"La palabra {mensaje} en mayúsculas es: {palabra_mayuscula}")

palabra_minuscula = mensaje.lower()

print(f"La palabra {mensaje} en minúsculas es: {palabra_minuscula}")
