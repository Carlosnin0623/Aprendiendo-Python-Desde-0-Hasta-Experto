# Revisar si una variable se encuentra dentro de rango 1 y 10

dato = int(input('Proporciona un dato entero:'))

# Revisamos si esta dentro de rango
#esta_dentro_rango = 1 <= dato <= 10
#print(f'Variable esta dentro de rango (entre 1 y 10)?: {esta_dentro_rango}')

# Revisamos la lógia inversa, si el dato esta fuera de rango

esta_dentro_rango = not (1 <= dato <= 10)
print(f'Variable esta fuera del rango (entre 1 y 10)?: {esta_dentro_rango}')