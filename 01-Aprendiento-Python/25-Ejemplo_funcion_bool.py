# Ejemplo 

# Error común de principiante

respuesta_usuario = "False" # Esto es texto

# La funcion bool evalúa si el string esta vacio como no esta vacio devolvera True
es_verdad = bool(respuesta_usuario) # Resultado: True porque "False" es un texto con 5 caracteres no esta vacio.

print(f"El valor es: {es_verdad}") # True

# Forma correcta de validar vacio:
texto_vacio = "" # Esto si indica que es false ya que no contiene ningun texto
print(bool(texto_vacio)) # Respuesta: False
