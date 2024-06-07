#########################################################################
# La Función input() es capaz de leer datos introducidos por el usuario,
# pasar esos datos al programa en ejecución, su resultado es una cadena
#########################################################################

# Función input sin argumento
print("Dime lo que sea..")
anything = input() # Esta función captura lo que el usuario escribe y lo guarda en una variable
print("Hmm...", anything,"... ¿en serio?")

# Función input con argumento
anything = input("\nDime lo que sea...") # El argumento es una cadena de texto
print("Hmm...", anything, "...¿en serio?")

# Uso de la función input en operaciones matematicas
anyting = float(input("\nIngresa un número: "))# la funcion int() o float() intenta convertir el valor capturado a número
something = anyting ** 2.0  
print(anything, "al cuagrado es ", something)


# Obtener la longitud de la hipotenusa, Teorema de pitagoras
print()
leg_a = float(input("Ingresa la longitud del primer cateto: "))
leg_b = float(input("Ingresa la longitud del segundo cateto: "))
print("La longitud de la hipotenusa es: ", (leg_a**2 + leg_b**2) ** .5)


##########################################################################
# Operador de contatenacion + (más), al ser aplicado a dos cadenas
# Operador de replicación * (asterisco), cuando es aplicado a una cadena y a un número
###########################################################################

# Concatenación
print()
fnam = input("¿Me puedes dar tu nombre por favor? ")
lnam = input("¿Me puedes dar tu apellido por favor? ")
print("Gracias. ")
print("\nTu nombre es " + fnam + " " + lnam + ".") # Concatenación de cadenas

# Replicación
print()
print("+" + 10 * "-" + "+") # Replicación 10 veces el guion y concatenación del mas
print(("|" + " " * 10 + "|\n") * 5, end="")
print("+" + 10 * "-" + "+")


##########################################################################
# Convertir de un número a una cadena str(number)
##########################################################################
print()
leg_a = float(input("Ingresa la longitud del primer cateto: "))
leg_b = float(input("Ingresa la longitud del segundo cateto: "))
print("La longitud de la hipotenusa es " + str((leg_a**2 + leg_b**2) ** .5)) # conversión de número a cadena


#########################################################################
# Ejercicio de prueba y = 1./(x + 1./(x + 1./(x + 1./x)))
#########################################################################

print()

x = float(input("Ingresa el valor para x: "))

y = 1./(x + 1./(x + 1./(x + 1./x)))

print("y =", y)

