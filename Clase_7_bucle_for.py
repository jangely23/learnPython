# puede "explorar" grandes colecciones de datos elemento por elemento

for i in range(10):
    print("El valor de i es", i)

for i in range(2, 8):
    print("El valor de i es", i)

for i in range(2, 8, 3):
    print("El valor de i es", i)

power = 1
for expo in range(16):
    print("2 a la potencia de", expo, "es", power)
    power *= 2

power = 1
for expo in range(16):
    print("2 a la potencia de", expo, "es", power)
    power *= 2

danger = 1
print("\nla tabla de ", danger )
for multiplicacion in range(10):
    print("la tabla de 1 x ", multiplicacion, ": ", danger * multiplicacion )

##############################################################################
#
# dulces sintácticos o azúcar sintáctica
# sentencia break y continue

# break - ejemplo

print("La instrucción break:")
for i in range(1, 6):
    if i == 3:
        break
    print("Dentro del bucle.", i)
print("Fuera del bucle.")


# continue - ejemplo

print("\nLa instrucción continue:")
for i in range(1, 6):
    if i == 3:
        continue
    print("Dentro del bucle.", i)
print("Fuera del bucle.")



# otro ejemplo break

largest_number = -99999999
counter = 0

while True:
    number = int(input("Ingresa un número o escribe -1 para finalizar el programa: "))
    if number == -1:
        break
    counter += 1
    if number > largest_number:
        largest_number = number

if counter != 0:
    print("El número más grande es", largest_number)
else:
    print("No has ingresado ningún número.")


# otro ejmeplo continue

largest_number = -99999999
counter = 0

number = int(input("Ingresa un número o escribe -1 para finalizar el programa: "))

while number != -1:
    if number == -1:
        continue
    counter += 1

    if number > largest_number:
        largest_number = number
    number = int(input("Ingresa un número o escribe -1 para finalizar el programa: "))

if counter:
    print("El número más grande es", largest_number)
else:
    print("No has ingresado ningún número.")



# otro ejemplo continue

word_without_vowels = ""

# Indicar al usuario que ingrese una palabra
# y asignarla a la variable user_word.

user_word = input("Digite una palabra: ")
user_word = user_word.upper()

for letter in user_word:
    # Completa el cuerpo del bucle.
    if letter == "A":
        continue
    elif letter == "E":
        continue
    elif letter == "I":
        continue
    elif letter == "O":
        continue
    else:
        word_without_vowels += letter
        
print(word_without_vowels)


# El bucle while y el bloque else: La rama else del bucle siempre se ejecuta una vez,
# independientemente de si el bucle ha entrado o no en su cuerpo.

i = 1
while i < 5:
    print(i)
    i += 1
else:
    print("else:", i)


i = 5
while i < 5:
    print(i)
    i += 1
else:
    print("else:", i)


# en el for La variable i conserva su último valor.

for i in range(5):
    print(i)
else:
    print("else:", i)



i = 111
for i in range(2, 1):
    print(i)
else:
    print("else:", i)
