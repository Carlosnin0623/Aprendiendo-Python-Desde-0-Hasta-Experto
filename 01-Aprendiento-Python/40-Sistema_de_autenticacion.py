"""
Sistema de Autenticación

Crea un programa para validar el usuario y contraseña proporcionados por el usuario.

Crear 2 constantes con los valores correctos y posteriormente compara
el usuario y password proporcionados por el usuario sean validos.
"""

USUARIO_VALIDO = "cnin"
PASSWORD_USUARIO = "12345"

usuario = input('Ingresa el nombre de usuario: ')
password = input('Ingresa tu contraseña: ')

validar_usuario = ((usuario.strip().lower() == USUARIO_VALIDO.strip().lower()) and (password.strip().lower() == PASSWORD_USUARIO.strip().lower()))

print(f'Los datos son correctos?: {validar_usuario}')