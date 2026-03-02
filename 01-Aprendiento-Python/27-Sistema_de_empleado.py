"""
Crea un programa para solicitar la informacion de un empleado, introduciendo
los datos por consola:

* Nombre empleado
* Edad de empleado (Convertir a entero)
* Salario del empleado (Convertir a flotante)
* Es jefe del departamento (Si / No)
"""

nombre_empleado = input("Escribe el nombre del empleado: ")
edad_empleado = int(input("Escribe la edad del empleado: "))
salario_empleado = float(input("Digita el salario del empleado: "))
es_jefe_departamento = input("Es jefe de departamento (Si/No)? ")

# Vamos a convertir a un tipo bool la variable es_jefe_departamento

es_jefe_departamento = es_jefe_departamento.lower() == 'si'

# imprimir los valores por consola
print('\n Datos del empleado')
print(f'Nombre: {nombre_empleado}')
print(f'Edad: {edad_empleado}')
print(f'Salario: {salario_empleado:.2f}') # con esto :.2f indicamos que queremos que se muestre 2 decimales y que es flotante
print(f'Es jefe del departamento?: {es_jefe_departamento}')
