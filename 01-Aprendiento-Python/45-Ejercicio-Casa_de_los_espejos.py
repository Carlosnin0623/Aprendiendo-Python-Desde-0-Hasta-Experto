"""
Casa de los Espejos

Supón que estas en un parque de diversiones y quieres entrar a la casa de los espejos.

Sin embargo debes cumplir con algunas condiciones.

 1. Debes tener más de 10 años.
 2. No debe darte miedo la oscuridad.

Si se cumplen las condiciones anteriores puedes entrar.

Para realizar este ejemplo vamos a utilizar al operador not para aplicar una lógica inversa.
"""

EDAD_MINIMA = 10

edad = int(input('Introduce tu edad:'))
tienes_miedo_oscuridad = input('Tienes miedo a la oscuridad: (Si / No)?')
tienes_miedo_oscuridad = tienes_miedo_oscuridad.strip().lower() == 'si'

if not tienes_miedo_oscuridad and edad >= 10:
    print('Puedes entrar a la Casa de los Espejos')
else:
    print('Lo siento la Casa de los Espejos podría darte miedo')

