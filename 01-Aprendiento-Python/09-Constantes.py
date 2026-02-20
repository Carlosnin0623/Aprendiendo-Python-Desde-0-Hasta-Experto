import math


"""
A diferencia de otros lenguajes de programación, en python no existe un tipo especifico
para definir una constante de manera estricta. Solo es una convención.

Python no impide cambiar el valor de una variable, pero podemos seguir la siguiente convención de declarar
el nombre de una variable en mayúsculas y con ello indicamos que el valor de esta variable no debe modificarse
una vez inicializada, es decir, esta variable se debe tratar como una constante.

"""

# Sintaxis para una constante
NOMBRE_CONSTANTE = "Eduardo" 

# Ejemplos de constantes 

MENSAJE_ERROR = 'Usuario Inválido'
NOMBRE_USUARIO_VALIDO = 'Admin'

# No debemos modificar el valor de una constante
PI = 3.14159
print('El valor de PI es:', PI)

NOMBRE_BASE_DATOS = 'clientesdb'
print('El nombre de la base de datos es:', NOMBRE_BASE_DATOS)

# usar una constante del lenguaje python, aunque en este caso no esta en mayusculas

print('Valor de math.pi', math.pi)