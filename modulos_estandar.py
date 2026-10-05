# Importación de módulo completo
import math

resultado = math.sqrt(25)
print(resultado)  # Imprime 5.0

# Importación de una función específica
from math import sqrt

resultado = sqrt(25)
print(resultado)  # Imprime 5.0

# --- Funciones y clases de módulos estándar ---
import random
import datetime

# Módulo random: generar número entero aleatorio entre 1 y 10
numero_aleatorio = random.randint(1, 10)
print(numero_aleatorio)  # Imprime un número entero aleatorio entre 1 y 10

# Módulo datetime: obtener fecha y hora actual
fecha_actual = datetime.datetime.now()
print(fecha_actual)  # Imprime la fecha y hora actual
