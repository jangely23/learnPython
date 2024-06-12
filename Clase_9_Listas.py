# Las listas son variables de multiples elementos, cada elemento es un escalar
# Cada uno de los elementos se identifica con un indice que inicia en 0 o que puede ser cualquier otra cosa


# Esto es una lista que consta de 5 valores numericos
numbers = [10, 5, 7, 2, 1]

# Cambiar el valor de una elemento de la lista
print("Contenido de la lista: ", numbers)
numbers[0] = 111  # Modifica el primer elemento de la lista
print("Nuevo contenido de la lista: ", numbers)

# Copiar el valor de un elemento a otro
numbers[1] = numbers[4]  # Copia el valor del quito elemento al segundo elemento de la lista
print("Nuevo contenido de la lista modificada: ", numbers)

# Acceder al contenido de la lista
print("\nLongitud de la lista: ", len(numbers))  # muestra la longitud de la lista
print("\nEl trecer (3) elemento de la lista es: ", numbers[2])

# Eliminando elementos de la lista
del numbers[1]
print("Longitud actual: ", len(numbers))  # Esto es una lista que consta de 5 valores)
print("Elementos actuales: ", numbers)

# Indices negativos, el indice -1 es el ultimo de la lista, el -2 es el anterior al ultimo
print("\nUltimo número: ", numbers[-1])
print("penultimo número: ", numbers[-2])

#######################################
# ejercicio de ejemplo
#######################################
hat_list = [1, 2, 3, 4, 5]  # Esta es una lista existente de números ocultos en el sombrero.

print("Longitud inicial", len(hat_list))

user_number = input("Digite un numero a ingresar: ")

# Paso 1: escribir una línea de código que solicite al usuario que reemplace el número central en la lista con un número entero ingresado por el usuario
hat_list[len(hat_list) // 2 ] = user_number

# Paso 2: escribe aquí una línea de código que elimine el último elemento de la lista.
del hat_list[-1]

# Paso 3: escribe aquí una línea de código que imprima la longitud de la lista existente.
print("Longitud actual", len(hat_list))

print(hat_list)
