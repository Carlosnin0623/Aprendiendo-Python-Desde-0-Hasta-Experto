# 1. Enteros (int): Números exactos sin decimales
vidas_jugador = 3
puntos_totales = 1500

# 2. Flotantes (float): Números con precisión decimal
precio = 19.99
pi = 3.1416
temperatura = -5.5

# ojo 10 es int, pero 10.0 es float

# 3. Strings (str): Secuencias de caracteres 
# Siempre van entre comillas (dobles o simples)

curso = "Curso de Python"
nivel = 'Principiante'

# Esto es texto, No un número (como un código postal):
codigo_postal = "28013"

# print(codigo_postal + 5) -> Error!

# 4. Booleanos (bool): Interruptores Lógicos

# Solo existen dos valores posibles

# La primera letra debe ser mayúscula.

es_divertido = True
esta_lloviendo = False

game_over = False
usuario_logueado = True

# ¿No estáas seguro del tipo de un dato?
# ! Preguntale a Python 

x = 10
y = "10"

print(type(x)) # Salida: class 'int'>
print(type(y)) # Salida: <class 'str'>

# Es muy útil para depurar errores. 
