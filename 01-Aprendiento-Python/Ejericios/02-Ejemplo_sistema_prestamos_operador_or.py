"""
Sistema Préstamo de Libros

Se pide crear un sistema para una bibliteca, la cual desea prestar libros si cumple
con cualquiera de las siguientes condiciones.

1. El usuario tiene credencial de estudiante.
2. El usuario vive a no más de 3 km a la redonda.

Si cumple con cualquiera de estas condiciones se le puede prestar el libro.
"""

print('\n*** Sistema Préstamo de Libros ***\n')
usuario_credencial_estudiante = input('El usuario posee credencial de estudiante?  Si / No?: ')
distancia_usuario = int(input)

respuesta = (usuario_credencial_estudiante.lower() == 'si' or distancia_usuario.lower() == 'no')

print(f'El usuario puede llevarse los libros?: {respuesta}')
