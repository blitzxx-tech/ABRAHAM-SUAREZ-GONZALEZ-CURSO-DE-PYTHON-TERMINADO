# --- Entrada de datos del usuario ---
nombre = input("Ingresa tu nombre: ")
edad = input("Ingresa tu edad: ")

print("Hola, " + nombre + "!")
print("Tienes " + edad + " años.")

# Conversión de tipos con input()
print("\n--- Conversión de tipo a entero con int() ---")
edad = int(input("Ingresa tu edad: "))

if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")

# --- Salida de datos formateada (f-strings) ---
print("\n--- Salida de datos con f-strings ---")
nombre = "Juan"
edad = 25

print(f"Hola, mi nombre es {nombre} y tengo {edad} años.")
