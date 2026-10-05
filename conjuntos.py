# --- Creación y operaciones básicas con conjuntos (Sets) ---
# Se pueden crear con llaves {} o con la función set()
frutas = {"manzana", "banana", "naranja"}
numeros = set([1, 2, 3, 4, 5])

conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}

# Unión (|)
union = conjunto1 | conjunto2
print(union)  # Imprime {1, 2, 3, 4, 5}

# Intersección (&)
interseccion = conjunto1 & conjunto2
print(interseccion)  # Imprime {3}

# Diferencia (-)
diferencia = conjunto1 - conjunto2
print(diferencia)  # Imprime {1, 2}

# Diferencia simétrica (^)
diferencia_simetrica = conjunto1 ^ conjunto2
print(diferencia_simetrica)  # Imprime {1, 2, 4, 5}

print("\n--- Métodos de conjuntos ---")
frutas = {"manzana", "banana", "naranja"}

# add(): agrega un elemento
frutas.add("pera")
print(frutas)  # Imprime {"manzana", "banana", "naranja", "pera"}

# remove(): elimina un elemento. Si no existe, genera error.
frutas.remove("banana")
print(frutas)  # Imprime {"manzana", "naranja", "pera"}

# discard(): elimina un elemento si está presente. Si no existe, no genera error.
frutas.discard("uva")
print(frutas)  # Imprime {"manzana", "naranja", "pera"}

# clear(): elimina todos los elementos del conjunto
frutas.clear()
print(frutas)  # Imprime set()
