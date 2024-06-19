# Comprención de listas 
# sintaxis especial utilizada por Python para completar o llenar listas masivas.
# Una comprensión de lista es en realidad una lista, pero se creó sobre la marcha 
# durante la ejecución del programa, y ​​no se describe de forma estática .
# por ejemplo:
# row = [PEON_BLANCO for i in range(8)] los datos que se utilizarán para completar la lista (PEON_BLANCO)
# la cláusula especifica cuántas veces se producen los datos dentro de la lista (para i en el rango(8))

# Genera una lista de diez elementos y la rellena con cuadrados de diez números
squares = [x ** 2 for x in range(10)] # el resultado: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Crea una lista de números impares de la lista squares
odds = [x for x in squares if x % 2 != 0 ] # el resultado: [1, 9, 25, 49, 81]

print(odds)
 
# Comprension de listas anidadas
# Ejemplo sin comprensión de listas:
# board = [] 
# for i in range(8):
#     row = [EMPTY for i in range(8)]
#     board.append(row)
# Ejemplo con comprensión de listas:
board = [[False for i in range(8)] for j in range(8)] # La parte interna crea una fila, y la parte externa crea una lista de filas.

