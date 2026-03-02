# Ejemplo 

# Error común de principiante

respuesta_usuario = "False" # Esto es texto

# La funcion bool evalúa si el string esta vacio, pero como no esta vacio... entonces devolvera True
es_verdad = bool(respuesta_usuario) # Resultado: True porque tiene 5 caracteres si estuviera vacio fuera False
print(f"El valor es: {es_verdad}") # True

# Forma correcta de validar vacio:
texto_vacio = "" # Esto si indica que es false ya que no contiene ningun texto
print(bool(texto_vacio)) # Respuesta: False
