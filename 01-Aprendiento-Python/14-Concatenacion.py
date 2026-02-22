"""
Que es concatenar?

Es el proceso de unir o más cadenas para formar una sola 
secuencia logica.
"""

# 1. Usando el operador +

nombre = "Lucia"
apellido = "García"
nombre_completo = nombre + " " + apellido
print("Mi nombre es:", nombre_completo)


#2. Usando el método print

edad = 28
print("Usamos comas:", "Nombre", nombre_completo, "Edad:", edad)

#3. Usando f-strings el mas recomendado actualmente
ciudad = "Barcelona"
pais = "España"
profesion = "Ingeniera"
presentacion = f"Hola, soy {nombre_completo}, tengo {edad + 1} años y soy {profesion} en {ciudad}, {pais}"

presentacion2 = f"""
Hola, soy {nombre_completo}, tengo {edad} años y soy {profesion}
en {ciudad}, {pais}
"""

print(presentacion)
print(presentacion2)