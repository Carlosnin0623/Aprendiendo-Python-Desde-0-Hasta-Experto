# Programa: Registro de explorador espacial 
 
# Objetivo: Crear variables con nombres válidos y claros

# CORRECTO: snake_case (minúsculas + guiones bajos)
nombre_explorador = 'Luna Vega'
planeta_origen = 'Marte'
edad_explorador = 29
misiones_completadas = 4
nivel_energia = 87.5

# for = 15  Esto arroja error (no debemos usar keywords o palabras reservadas)
Nivel_Energia = 90.5 # No es una buena practia

"""
Constantes: En python no existe como tal el concepto de constantes, solo que hacen los programadores de Python
es poner las variables que consideren como constantes en mayúsculas y ya con esto indican que es una variable
donde su valor no debe cambiar.

"""
NIVEL_ENERGIA = 100.00  # Esto se considera una constante en python
nivel_energía = 80.0 # no se deben usar caracteres especiales (acentos, ñ)
print("=== Ficha del Explorador ===")
print("Nombre explorador:", nombre_explorador)
print("Planeta de origen:", planeta_origen)
print("Edad explorador:", edad_explorador)
print("Misiones completadas:", misiones_completadas)
print("Nivel de energía:", nivel_energia)
