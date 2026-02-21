# El problema de la Ambiguedad

# Cuando usas comillas dentro de comillas del mismo tipo, rompes la cadena de texto


#mensaje = "Ella dijo "Hola" al entrar"
#print(mensaje)


# Solucionado escapando las comillas internas
mensaje = "Ella dijo \"Hola\" al entrar"
print(mensaje)


# Carácter especial \n Nueva Linea
# Este carácter obliga al texto a saltar al renglón de abajo, como presionar 'Enter'.

saludar = "Hola\nmundo"
print(saludar)

# Carácter especial \t Tabulación
# Salta a la siguiente 'parada de tabulación' (cada 4 u 8 espacios, según tu editor) para crear columnas ordenadas

nombre = "Nombre:\tJuan"
apellido = "Apellido:\tPérez"
print(nombre)
print(apellido)

#Carácter especial \' Comillas simples

# Esencial cuando tu string está delimitado por comillas simples y quieres usar un
# apóstrofo dentro.

# Escapando el apóstrofo en el apellido

apellido2 = 'Jose O\'Gorman'
print(apellido2)