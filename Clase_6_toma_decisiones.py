
#########################################################
# Sentencia condicional, palabra reservada if, las      #
# instrucciones se ejecutan si la validacion es True    #
# si la validacion es False se ejecuta el else          #
#########################################################
#                                                       #  
#     if true_or_false_condition:                       #
#        perform_if_condition_true                      #
#     else:                                             #
#        perform_if_condition_false                     #
#                                                       #
#########################################################
# Sentencias condicionales anidadas                     # 
#########################################################
#                                                       #
#    if the_weather_is_good:                            #
#        if nice_restaurant_is_found:                   #
#            have_lunch()                               #
#        else:                                          #
#            eat_a_sandwich()                           #
#    else:                                              #
#        if tickets_are_available:                      #
#            go_to_the_theater()                        #
#        else:                                          #
#            go_shopping()                              #
#                                                       #
#########################################################
# Ejemplo 1                                             #
#########################################################

# Se leen dos números                                    
number1 = int(input("Ingresa el primer número: "))
number2 = int(input("Ingresa el segundo número: "))
 
# Elige el número más grande
if number1 > number2:
    larger_number = number1
else:
    larger_number = number2
 
# Imprime el resultado
print("El número más grande es:", larger_number)


#########################################################
# Ejemplo 2                                             #
#########################################################

# Se leen dos números
number1 = int(input("Ingresa el primer número: "))
number2 = int(input("Ingresa el segundo número: "))
 
# Elige el número más grande
if number1 > number2: larger_number = number1
else: larger_number = number2
 
# Imprime el resultado
print("El número más grande es:", larger_number)

 
#########################################################
# Ejemplo 3                                             #
#########################################################

# Se leen tres números
number1 = int(input("Ingresa el primer número: "))
number2 = int(input("Ingresa el segundo número: "))
number3 = int(input("Ingresa el tercer número: "))
 
# Asumimos temporalmente que el primer número
# es el más grande.
# Lo verificaremos pronto.
largest_number = number1
 
# Comprobamos si el segundo número es más grande que el mayor número actual
# y actualiza el número más grande si es necesario.
if number2 > largest_number:
    largest_number = number2
 
# Comprobamos si el tercer número es más grande que el mayor número actual
# y actualiza el número más grande si es necesario.
if number3 > largest_number:
    largest_number = number3
 
# Imprime el resultado.
print("El número más grande es:", largest_number)
 





