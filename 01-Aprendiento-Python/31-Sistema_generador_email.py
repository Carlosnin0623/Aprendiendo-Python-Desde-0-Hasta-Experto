"""
Sistema Generador de Emails

Se solicita crear una nueva versión del sistema generador de emails.

Para generar un email se debe solicitar

Nombre: Juan Carlos
Apellidos: Gómez Lara
Nombre empresa: Global Mentoring
Extensión Dominio: .com.mx

El resultado debe ser:
juan.carlos.gomez.lara@globalmentorin.com.mx
"""

nombre_usuario = "Juan Carlos"
apellido_usuario = "Gómez Lara"
nombre_empresa = "Global Mentoring"
extension_dominio = ".com.mx"

nombre_usuario = nombre_usuario.strip().replace(" ",".").lower()
print(nombre_usuario)

apellido_usuario = apellido_usuario.strip().replace("ó","o").replace(" ",".").lower()
print(apellido_usuario)

nombre_empresa = nombre_empresa.strip().replace(" ","").lower()
print(nombre_empresa)

print(f"{nombre_usuario}.{apellido_usuario}@{nombre_empresa}{extension_dominio}")