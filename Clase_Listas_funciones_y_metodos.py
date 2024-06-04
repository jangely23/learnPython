"""
    Un método es un tipo especifico de funcion
    Se comporta como una función, se parece a una función
    pero difiere en la forma en que actua y su estilo de invocación.

    la función no pertenece a ningun dato, ella obtiene datos, puede crear datos
    y produce un resultado.

    Un metodo hace eso mismo pero tambien puede cambiar el estado de una entidad seleccionada.
    Un método es propiedad de los datos para los que trabaja, mientras que una función es
    propiedad de todo el codigo.

    En general, una invocación de función típica puede tener este aspecto:

    result = function(arg)

    La función toma un argumento, hace algo, y devuelve un resultado.

    Una invocación de un método típico usualmente se ve así:

    result = data.method(arg)
"""

# Agregar elementos a una lista
numbers = [111, 7, 2, 1]
print("Longitud incial: ", len(numbers))
print("Contenido inicial: ", numbers)

print("\nSe adiciona el 4")
numbers.append(4)  # Agrega un nuevo elemento
print("Nueva longitud: ", len(numbers))
print("Nuevo contenido: ", numbers)

print("\nSe inserta el 222 en el index 0")
numbers.insert(0, 222)  # Agrega un nuevo elemento en la posicion indicada
print("Longitud actual: ", len(numbers))
print("Contenido actual: ", numbers)

###########################################
# Lista vacia - agregar elementos con for
###########################################

my_list = []

for i in range(5):
    my_list.append(i + 1)

print("\nLista generada desde un for con append: ",my_list)

######

my_list2 = []  # Creando una lista vacía.

for i in range(5):
    my_list2.insert(0, i + 1)

print("\nLista generada desde un for con insert: ", my_list2)

######

# recorrer una lista con for

my_list3 = [10, 1, 8, 3, 5]
total = 0

for i in range(len(my_list3)):
    total += my_list3[i]

print("\nSuma de la ultima lista usando for: ", total)

# otra forma de usar for
total2 = 0

for i in my_list3:
    total2 += i

print("\nSuma de la ultima lista usando la indexacion del for: ", total2)

#######################################
# INtercambiar elementos de la lista
#######################################

# acción para pocos elementos
my_list4 = [10, 1, 8, 3, 5]

my_list4[0], my_list4[4] = my_list4[4], my_list4[0]
my_list4[1], my_list4[3] = my_list4[3], my_list4[1]

print(my_list4)

# acción para muchos elementos
my_list5 = [10, 1, 8, 3, 5]
print("\nMi lista para intercambiar valores con for: ", my_list5)

for i in range( len(my_list5) // 2):
    my_list5[i], my_list5[ len(my_list5) - i - 1] = my_list5[ len(my_list5) - i - 1], my_list5[i]

print("Mi lista con valores intercambiados usando for: ", my_list5)


