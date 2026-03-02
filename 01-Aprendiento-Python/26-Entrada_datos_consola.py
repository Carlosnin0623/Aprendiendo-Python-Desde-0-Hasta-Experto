"""
Que es input?

Es la función que permite que tu programa deje de hablar y empiece a escuchar.

Nota: La función input siempre devolvera un string, aunque escribas números.
"""
nombre = input("Escribe tu nombre: ")

# Forma correcta de convertir los datos que entran por consola (int o float)
edad = int(input("Escribe tu edad: "))

# Flotante
altura = float(input("Digita tu altura: "))

print(f"Tú nombres es {nombre}, tu edad es: {edad} y tu altura es: {altura}")
