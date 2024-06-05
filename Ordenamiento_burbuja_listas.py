"""
Algorimo sencillo pero poco eficiente
Raramente se usa y en listas cortas como:
[8, 10, 6, 2, 4]
ordenar de forma ascendente
tomaremos el primer y el segundo elemento y los compararemos;
si determinamos que están en el orden incorrecto (es decir, el primero es mayor que el segundo),
los intercambiaremos; si su orden es válido, no haremos nada.
"""

lista = [8, 10, 6, 2, 4, 34, 1, 434, 3]
cambio = True  # Permite el control del bucle
print("Lista sin ordenar: ", lista)

while cambio:
    cambio = False # No hay intercambio
    for i in range(len(lista)-1):
        if lista[i] > lista[i + 1]:
            cambio = True # Se necesita intercambio
            lista[i], lista[i + 1] = lista[i + 1], lista[i]

print("lista ordenada: ", lista)

########################################################################
# Ejemplo inetractuando con usuario
########################################################################
my_list = []
swapped = True
num = int(input("¿Cuántos elementos deseas ordenar?: "))

for i in range(num):
    val = float(input("Ingresa un elemento de la lista: "))
    my_list.append(val)

while swapped:
    swapped = False
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print("\nOrdenada:")
print(my_list)

########################################################################
# Ejemplo usando herramientas de Python
########################################################################

my_list_prueba = [8, 10, 6, 2, 4]
print("\nLista sin ordenar: ", my_list_prueba)

my_list_prueba.sort()

print("\nOrdenada:")
print(my_list_prueba)