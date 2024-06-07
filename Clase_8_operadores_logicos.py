##########################################################################################
# familiarizado con las leyes de De Morgan. Dicen que:
# La negación de una conjunción es la separación de las negaciones.
# La negación de una disyunción es la conjunción de las negaciones.


# Los operadores lógicos toman sus argumentos como un todo, independientemente
# de cuantos bits contengan. Los operadores solo conocen el valor: cero 
# (cuando todos los bits se restablecen) significa False; no cero 
# (cuando se establece al menos un bit) significa True.

# operador de conjunción lógica en Python es la palabra and, ejemplo: counter > 0 and value == 100
# Un operador de disyunción es la palabra or.
# operador not, operador unario que realiza una negación lógica. Su funcionamiento es simple: convierte la verdad en falso y lo falso en verdad.
# los operadores lógicos no penetran en el nivel de bits de su argumento. Solo les interesa el valor entero final.

var = 1

# Ejemplo 1:
print(var > 0)
print(not (var <= 0))
 
 
# Ejemplo 2:
print(var != 0)
print(not (var == 0))

# Ejemplo 3:
i = 1
j = not not i

print("\n\n")

##############################################################################################
# operadores bit a bit ó bitwise, permiten manipular bits de datos individuales
# & (ampersand) ‒ conjunción a nivel de bits;
# | (barra vertical) - disyunción a nivel de bits;
# ~ (tilde) - negación a nivel de bits;
# ^ (signo de intercalación) - o exclusivo a nivel de bits (xor).
# los argumentos de estos operadores deben ser enteros; no debemos usar flotantes aquí.
# Los operadores bit a bit son más estrictos: tratan con cada bit por separado. 

i = 15
j = 22

log = i and j  # es iual a True

# es compara bit a bit lo queda un resultado de  
# i =   01111
# j =   10110
# bit = 00110

bit = i & j  # es igual a 6 en binario 00110

# negacion logica
logneg = not i

# negacion bit a bit
bitneg = ~i

print("\n\n")

#################################################################################################################
# Como trabajar con bits individuales 
# Se te ha dicho que puedes usar una variable asignada de la siguiente forma: flag_register = 0x1234
# Cada bit de la variable almacena un valor de si/no.
# uno de estos bits es tuyo - el tercero : flag_register = 0000000000000000000000000000x000

flag_register = 0x1234

# Construyamos una máscara de bits para detectar el estado de tus bits. 
# Debería apuntar a el tercer bit. Ese bit tiene el peso de 2**3=8. 

flag_register = flag_register & 1 

the_mask = 8 


print(bin(flag_register))

# comprobar el estado de un bit
if flag_register & the_mask:
    print("Mi bit se estableció en 1.")
else:
    print("Mi bit se restableció a 0.")

# establecer el bit asignado
# flag_register = flag_register | the_mask

flag_register |= the_mask

# comprobar el estado de un bit
if flag_register & the_mask:
    print("Mi bit se estableció en 1.")
else:
    print("Mi bit se restableció a 0.")

# reiniciar el bit asignado
# flag_register = flag_register & ~the_mask

flag_register &= ~the_mask

# comprobar el estado de un bit
if flag_register & the_mask:
    print("Mi bit se estableció en 1.")
else:
    print("Mi bit se restableció a 0.")

# negar el bit asignado
# flag_register = flag_register ^ the_mask

flag_register ^= the_mask

# comprobar el estado de un bit
if flag_register & the_mask:
    print("Mi bit se estableció en 1.")
else:
    print("Mi bit se restableció a 0.")


###########################################################################################################
# Desplazamiento binario a la izquierda y desplazamiento binario a la derecha (shifting. )
# desplazar un valor un bit a la izquierda corresponde a multiplicarlo por dos; respectivamente, 
# desplazar un bit a la derecha es como dividir entre dos (observa que se pierde el bit más a la derecha).
# Los operadores de cambio en Python son un par de dígrafos: < < y > >, sugiriendo claramente en qué dirección actuará el cambio

var = 17
print("binario numero original: ",bin(17))

var_right = var >> 1
print("binario desplazamiento a la derecha: ", bin(var_right))

var_left = var << 2
print("binario desplazamiento a la izquierda: ", bin(var_left))

print("original: ", var, " desplazado a la derecha: ", var_right , " desplazado a la izquierda: ", var_left)


##############################################################################################################
# resumen de la clase

print(
    """ 
        1. Python es compatible con los siguientes operadores lógicos:

        and → si ambos operandos son verdaderos, la condición es verdadera, por ejemplo, (True and True) es True.
        or → si alguno de los operandos es verdadero, la condición es verdadera, por ejemplo, (True or False) es True.
        not → devuelve False si el resultado es verdadero y devuelve True si es falso, por ejemplo, not True es False.
        2. Puedes utilizar operadores bit a bit para manipular bits de datos individuales. Los siguientes datos de muestra:

        x = 15, el cual es 0000 1111 en binario,
        y = 16, el cual es 0001 0000 en binario.
        Se utilizarán para ilustrar el significado de operadores bit a bit en Python. Analiza los ejemplos a continuación:

        & hace un bit a bit and (y), por ejemplo, x & y = 0, el cual es 0000 0000 en binario,
        | hace un bit a bit or (o), por ejemplo, x | y = 31, el cual es 0001 1111 en binario,
        ˜ hace un bit a bit not (no), por ejemplo, ˜ x = 240*, el cual es 1111 0000 en binario,
        ^ hace un bit a bit xor, por ejemplo, x ^ y = 31, el cual es 0001 1111 en binario,
        >> hace un desplazamiento bit a bit a la derecha, por ejemplo, y >> 1 = 8, el cual es 0000 1000 en binario,
        << hace un desplazamiento bit a bit a la izquierda, por ejemplo, y << 3 = 128, el cual es 1000 0000 en binario. 
    """
)