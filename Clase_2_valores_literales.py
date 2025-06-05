###### Literales Python ######
######################################################################
#  Los literales son valores constantes que se asignan a variables.  #     
#  se utilizan para codificar datos y ponerlos dentro del codigo     #
######################################################################

# La característica del valor numérico que determina el tipo, rango y aplicación se denomina el tipo.
# Si se codifica un literal y se coloca dentro del código de Python, la forma del literal determina 
# la representación (tipo) que Python utilizará para almacenarlo en la memoria.

# Se almacenan en la memoria de la siguiente manera:
print("2") # cadena
print(2) # entero   

# Python permite el uso de guion bajo en los literales numéricos y el signo + o - para indicar el signo.
print(1_000_000) # un millón
print(-1_000_000.0) # un millón en negativo con decimales
print(+1_000_000.0) # un millón en positivo con decimales

# Números octales y hexadecimales
# Si un número entero esta precedido por un código 0O o 0o (cero-o), el número será tratado como un valor octal. 
# Esto significa que el número debe contener dígitos en el rango del [0..7] únicamente.
print("Numeros octales")
print(0o123) # 0 octal numero 83 en decimal

# Si un número entero esta precedido por un código 0X o 0x (cero-x), el número será tratado como un valor hexadecimal. 
# Esto significa que el número debe contener dígitos en el rango del [0..9] y las letras del [a..f] o [A..F] únicamente.
print("Numeros hexadecimales")
print(0x123) # 0x hexadecimal numero 291 en decimal

# Números flotantes
# Son números que tienen (o pueden tener) una parte fraccionaria después del punto decimal
# Cuando se usan términos como dos y medio o menos cero punto cuatro, pensamos en números 
# que la computadora considera como números punto-flotante
# Python soporta números punto-flotante con notación científica.
# El separador decimal es un punto, no una coma.
print("\nNumeros de coma flotante")
print(.4) #se puede omitir el cero cuando es el único dígito antes del punto decimal
print(4.) #se puede omitir el cero cuando es el único dígito después del punto decimal
print(0.4)
print(4.0)
print(3E8) # tres por diez elevado a la octava potencia
print(3e8) # tres por diez elevado a la octava potencia
print(6.62607E-34) # La Constante de Planck
print(0.0000000000000000000001) # Python siempre elige la presentación más corta del número

# Cadenas
# Las cadenas son secuencias de caracteres.
# Las cadenas se escriben entre comillas simples o dobles.
# Las cadenas pueden contener caracteres especiales y secuencias de escape.
print("\nCadenas")
print("Me gusta \"Monty Python\"") #Una comilla precedida por una diagonal invertida cambia su significado - no es un limitador, simplemente es una comilla
print('Me gusta "Monty Python"') # utilizar una apóstrofe en lugar de una comilla
print('I\'m Monty Python') #Otra forma de escapar comillas
print("I'm Monty Python.")

# Boobleanos 
# Los booleanos son valores lógicos que representan verdadero o falso.
# Los booleanos se escriben como True (1) y False (0), se debe respetar las mayusculas.
# Los booleanos se utilizan para representar valores lógicos en Python. 
print("\nBooleanos True=1 ó False=0")
print(True > False) # True
print(True < False) # False

# None
# None es un valor especial que representa la ausencia de un valor.
# None es un valor que no tiene valor es llamado un objeto de NoneType.
print("\nNone")
print(None)


# Ejercicios de ejemplo
print('"Estoy"\n""aprendiendo""\n"""Python"""')
print("\"I'm\"\n\"\"learning\"\"\n\"\"\"Python\"\"\"")


