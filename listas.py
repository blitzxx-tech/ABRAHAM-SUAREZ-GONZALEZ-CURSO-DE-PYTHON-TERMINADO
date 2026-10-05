# --- Creación y acceso a listas ---
frutas = ["manzana", "banana", "naranja"]

# Acceso mediante índices positivos (comienzan en 0)
print(frutas[0])  # Imprime "manzana"
print(frutas[1])  # Imprime "banana"
print(frutas[2])  # Imprime "naranja"

# Acceso mediante índices negativos (-1 es el último elemento)
print(frutas[-1])  # Imprime "naranja"
print(frutas[-2])  # Imprime "banana"
print(frutas[-3])  # Imprime "manzana"

print("\n--- Métodos de listas ---")
# Reiniciamos la lista para los ejemplos de métodos
frutas = ["manzana", "banana", "naranja"]

# append(): agrega un elemento al final
frutas.append("pera")
print(frutas)  # Imprime ["manzana", "banana", "naranja", "pera"]

# insert(): inserta un elemento en una posición específica (índice 1)
frutas.insert(1, "uva")
print(frutas)  # Imprime ["manzana", "uva", "banana", "naranja", "pera"]

# remove(): elimina la primera aparición del elemento especificado
frutas.remove("banana")
print(frutas)  # Imprime ["manzana", "uva", "naranja", "pera"]

# pop(): elimina y retorna el elemento en el índice indicado (índice 2)
fruta_eliminada = frutas.pop(2)
print(frutas)  # Imprime ["manzana", "uva", "pera"]
print(fruta_eliminada)  # Imprime "naranja"

# sort(): ordena la lista alfabéticamente/numéricamente
frutas.sort()
print(frutas)  # Imprime ["manzana", "pera", "uva"]

# reverse(): invierte el orden actual de los elementos
frutas.reverse()
print(frutas)  # Imprime ["uva", "pera", "manzana"]
