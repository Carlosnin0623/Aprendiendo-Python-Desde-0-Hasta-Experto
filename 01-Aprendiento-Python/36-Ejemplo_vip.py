"""
Sistema Descuentos VIP

Una tienda de supermercado ofrece un descuento especial a clientes que compren
10 o más artículos por día y además sean miembros de la tienda.

El sistema debe solicitar al cliente que indique cuantos artículos ha comprado
en el día y preguntarle si cuenta con miembresía de la tienda.

En caso de haber comprado 10 o más productos y ser miembro de la tienda
entonces tendrá un acceso al descuento VIP
"""

print("\n*** Sistema de Supermercado ***\n")

NO_PRODUCTOS_DESCUENTOS = 10

cantidad_productos = int(input("Ingrese la cantidad de artículos que ha comprado: "))

tiene_membresia= input('Usted cuenta con la membresía de la tienda?... Si o no? ')

es_elegible_descuento = (cantidad_productos >= NO_PRODUCTOS_DESCUENTOS 
                         and tiene_membresia.lower() == 'si')

print(f'Tienes acceso al descuento VIP? {es_elegible_descuento}')