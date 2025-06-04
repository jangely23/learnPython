#######################################################
#                   print()                           #
#  La función print() es una función integrada        #
#  imprime/envía un mensaje específico a la           #
#  pantalla/ventana de consola.                       #
#  python tiene 69 funciones integradas.              #
#######################################################

# la forma posicional de pasar argumentos, muestra el significado de los argumentos en el orden en que se pasan
print("Ejecucion de ejemplos de la forma posicional de pasar argumentos:")
print("\nHola mundo \n") # el slash \ es un caracter de escape que anuncia que el siguiente carácter tiene un significado diferente 
print("¡Hola, Python!")
print("Greg")
print('Greg')
print("Jessica", "Leonel")  
print("La Witsi Witsi Araña" , "subió" , "a su telaraña.")  
print("Python") # Se almacena como una serie de letras
print(1234) # Esto es un literal se convierte a una serie de bits
print(11_111_111)#el número se puede escribir ya sea así: 11111111, o como sigue: 11_111_111.
print(-11111111)
print(True)
print({"dirección": "mz 51 cs 17"})
print("\\")
print()
print()

# la forma argumentos de palabras clave, el significado de los argumentos se define por la palabra clave usada para identificarlos
# elementos de una argumento de palabras clave:
#    1- Nombre del argumento: end, sep, file, flush
#       Significado del argumento:
#         end: se utiliza para especificar el final de la línea. Por defecto es "\n"
#         sep: se utiliza para especificar el separador entre los argumentos. Por defecto es " ".  
#         file: se utiliza para especificar el archivo en el que se imprimirá el texto. Por defecto es sys.stdout.
#         flush: se utiliza para especificar si se debe vaciar el buffer de salida. Por defecto es False.
#    2- el igual (=) se utiliza para asignar un valor a un argumento. 
#    3- el valor del argumento.
# Cualquier argumento de palabra clave debe colocarse después del último argumento posicional (esto es muy importante)

print("Ejecucion de ejemplos de la forma de palabras clave de pasar argumentos:")

# el argumento end=" " indica que el texto se imprimirá en la misma línea
print("Mi nombre es", "Python.", end=" ") 
print("Monty Python.")

# el argumento sep="-" indica que el texto se imprimirá separado por un guion
print("Mi", "nombre", "es", "Monty", "Python.", sep="-") 

# el argumento end="*" indica que el texto se imprimirá en la misma línea y se agregará un asterisco al final 
print("Mi", "nombre", "es", sep="_", end="*") 

print("Monty", "Python.", sep="*", end="*\n") # el argumento sep="*" indica que el texto se imprimirá separado por un asterisco y el argumento end="\n" indica que el texto se imprimirá en la siguiente línea

print("H","o","l","a","!", sep="", end=" ")
print("mundo")
print("mi","primer","programa", sep="_")
print()
print()

# Ejercicios de prueba
print("Ejecucion de ejercicios de prueba:")
###################
print("original version:")
###################
print("    *")
print("   * *")
print("  *   *")
print(" *     *")
print("***   ***")
print("  *   *")
print("  *   *")
print("  *****")
###################
print("with fewer (con menos) 'print()' invocations:")
###################
print("    *\n   * *\n  *   *\n *     *\n***   ***\n  *   *\n  *   *\n  *****")
print()
###################
print("higher (doble de grande):")
###################
print("        *")
print("       * *")
print("      *   *")
print("     *     *")
print("    *       *")
print("   *         *")
print("  *           *")
print(" *             *")
print("******     ******")
print("     *     *")
print("     *     *")
print("     *     *")
print("     *     *")
print("     *     *")
print("     *     *")
print("     *******")
print()

###################
print("doubled (duplica la flecha):")
###################
print("        *        "*2) # el asterisco se utiliza para repetir el texto
print("       * *       "*2)
print("      *   *      "*2)
print("     *     *     "*2)
print("    *       *    "*2)
print("   *         *   "*2)
print("  *           *  "*2)
print(" *             * "*2)
print("******     ******"*2)
print("     *     *     "*2)
print("     *     *     "*2)
print("     *     *     "*2)
print("     *     *     "*2)
print("     *     *     "*2)
print("     *     *     "*2)
print("     *******     "*2)
print()

######################################
#### error de syntaxis en print() ####

## print(Greg)   ## Error
## print"Greg"  ## Error
## print("\")  ## Error
## print("    *\n   * *\n  *   *\n *     *\n***   ***\n  *   *\n  *   *\n  *****") * 2 ## Error

######################################      
