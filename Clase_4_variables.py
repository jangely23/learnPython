## Ejecutame para ver el contenido ##

print("\nLas variables son contenedores que almacenan \ncualquier tipo de valor variable en el tiempo\n")
print("Se componen de un nombre y un valor\n")
print("El nombre puede tener: \n")
print("- Mayúsculas, minúsculas, dígitos y _ (guion bajo)")
print("- El nombre debe comenzar con una letra")
print("- El guion bajo se considera una letra")
print("- Son case sensitive, por ende 'valor' es diferente a 'VALOR'")
print("- El nombre debe ser diferente a las reservadas por Python")

print("\nConvención de nomenclatura para variables y funciones: \n")
print("- Los nombres de las variables deben estar en minúsculas, con palabras \n  separadas por guiones bajos para mejorar la legibilidad \n  (por ejemplo, var, my_variable)")
print("- Los nombres de las funciones siguen la misma convención que los \n  nombres de las variables (por ejemplo, fun, my_function)")
print("- También es posible usar letras mixtas (por ejemplo, myVariable), \n  pero solo en contextos donde ese ya es el estilo predominante, \n  para mantener la compatibilidad retroactiva con la convención adoptada.")

print("\nPalabras claves o reservadas por Python \n")
print("False, \nNone, \nTrue, \nand, \nas, \nassert, \nbreak, \nclass, \ncontinue, \ndef, \ndel, \nelif, \nelse, \nexcept, \nfinally, \nfor, \nfrom, \nglobal, \nif, \nimport, \nin, \nis, \nlambda, \nnonlocal, \nnot, \nor, \npass, \nraise, \nreturn, \ntry, \nwhile, \nwith, \nyield")

print("\nEn Python las variables se crean cuando se les asigna un valor,\nno es necesario declararlas. ")
print("para crearlas se usa la sintaxis nombre, igual, valor ejemplo: edad = 12")
print("se puede ver el contenido de esa variable con un print ejemplo: print(edad)")


#### Ejemplo teorema de Pitágoras ####
print("\nTeorema de pitagoras")
a = 3.0
b = 4.0
c = (a ** 2 + b ** 2) ** 0.5
print("cateto a=3.0, cateto b=4.0, hipotenusa c=(a ** 2 + b ** 2) ** 0.5")
print("el resultado es c =", c)

# Nota: necesitamos hacer uso del operador ** para evaluar la raíz cuadrada como:
# √ (x)  = x(½)
# y
# c = √ a2 + b2 


#### ejemplo 3x3 - 2x2 + 3x - 1 ####
print("\nEjercicio 3x3 - 2x2 + 3x - 1")
x = 1
x = float(x)
y = 3 * x**3 - 2 * x**2 + 3 * x - 1
print("el valor de x es 1")
print("el resultado es y =", y)
