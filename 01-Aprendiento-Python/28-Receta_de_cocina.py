"""
Receta de cocina

"""

nombre_receta = input("Escribe el nombre de la receta: ")
ingredientes_receta = input("Escribe los ingredientes de la receta: ")
duracion_receta = int(input("Ingresa el tiempo de duración de la receta en minutos: "))
dificultad_receta = input("Ingresa la dificultad de la receta: ")

print("\n *** Información Receta ***")
print(f"Nombre: {nombre_receta}")
print(f"Ingredientes: {ingredientes_receta}")
print(f"Duración: {duracion_receta}")
print(f"Dificultad: {dificultad_receta}")