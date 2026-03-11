"""
Aplicación de Salud y Fitnes

Se solicita crear una aplicación de salud y fitnes que solicite lo siguiente:

* Nombre del Usuario
* Pasos caminados en el día

Ademas definiremos las siguientes constantes:

META_PASOS_DIARIO = 10000
CALORIAS_POR_PASO = 0.04 # Valor aproximado en kilocalorias

Con los valores anteriores debemos calcular las calorias quemadas segun los pasos caminados.

calorias_quemadas = pasos_diarios * CALORIAS_POR_PASO

y verificaremos si se cumplio la meta de pasos diarios

meta_alcanzada = pasos_diarios >= META_PASOS_DIARIO

"""

# Datos de entrada del usuario
try:
    nombre_usuario = input('Introduzca su nombre de usuario: ').strip().lower()

    if not nombre_usuario:
        raise ValueError("El nombre de usuario no puede estar vacío")
    
      # validando que el usuario no tenga números al principio
    if(nombre_usuario[0].isdigit()):
      raise ValueError('El nombre de de usuario no puede comenzar con números')
    
    pasos_diarios = float(input('Introduce los pasos caminados el día de hoy: '))

    if pasos_diarios < 0:
        raise ValueError("Los pasos no pueden ser negativos")

    # Constantes
    META_PASOS_DIARIO = 10000
    CALORIAS_POR_PASO = 0.04

    calorias_quemadas = pasos_diarios * CALORIAS_POR_PASO

    meta_alcanzada = (
        f'Felicidades {nombre_usuario}!, alcanzaste la meta y quemaste {calorias_quemadas:.2f} calorias'
        if pasos_diarios >= META_PASOS_DIARIO
        else f'Lo siento {nombre_usuario}, no alcanzaste la meta hoy, pero quemaste {calorias_quemadas:.2f} calorias'
    )

    print(meta_alcanzada)

except ValueError as e:
    print(f'Error de datos: {e}')