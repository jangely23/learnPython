list_1 = [1]
print("\nContenido inicial de list_1: ", list_1)
list_2 = list_1[:] # crea una lista nueva con el contenido de list_1
list_3 = list_1 # se asigna la posicion en memoria de list_1, se asigna por referencia
print("\nValor copiado list_2 = list_1[:] : ", list_2)
print("Valor copiado list_3 = list_1 : ", list_3)
list_1[0] = 2
print("\nContenido modificado de list_1: ", list_1)
print("\nValor copiado list_2 = list_1[:] : ", list_2)
print("Valor copiado list_3 = list_1 : ", list_3)

# Ejemplo
#
my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:3] # crea una nueva lista con valores desde la posicion 1 hasta posicion 2 (3-1)
print("\nContenido de new_list: ", my_list)
print("Valor copiado new_list = my_list[1:3] : ",new_list)

print(5 in my_list)
print(5 not in my_list)
print(12 in my_list)
