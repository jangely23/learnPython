"""  
    Para encontrar cualquier elemento de una lista bidimensional, debes usar dos coordenadas :

    Una vertical (número de fila).
    Una horizontal (número de columna). 

"""
# Ejemplo:
# Un dispositivo registra la temperatura del aire cada hora 
# y lo hace durante todo el mes. 
# Esto te da un total de 24 × 31 = 744 valores. 
# diseña una lista capaz de almacenar todos estos resultados.

temperatura = [ [0.0 for hora in range(24) ] for dia in range(31) ]

# Toda la matriz temperatura está llena de ceros ahora. 
# Puede suponer que se actualiza automáticamente utilizando agentes de hardware especiales. 
# Lo que tienes que hacer es esperar a que la matriz se llene con las mediciones.
# Ahora determina la temperatura promedio mensual del mediodía:

total = 0.0

for dia in temperatura:
    total += dia[11]

promedio = (total/len(temperatura))

print("Temperatura promedio a medio dia es: ", promedio)

# Ahora se debe encontrar la temperatura mas alta
temperatura_alta = 0.0

for dia in temperatura:
    for temperatura_hora in dia:
        if temperatura_hora > temperatura_alta : 
            temperatura_alta = temperatura_hora

print("La temperatura mas alta fue: ", temperatura_alta)

# Contar los dias en que la temperatura supero los 20 grados
cantidad_dias = 0

for dia in temperatura:
    for temperatura_hora in dia:
        if temperatura_hora > 20.0:
            cantidad_dias += 1

print("Durante ", cantidad_dias, "los días fueron calurosos")

################################################################
# Arreglo tridimensionales
# Es un hotel enorme que consta de tres edificios, de 15 pisos cada uno. Hay 20 habitaciones en cada piso.
################################################################
rooms = [[[False for r in range(20)] for f in range(15)] for t in range(3)]

for t in rooms:
    print("\n\n\n",t)
    for f in t:
        print("\n\n",f)
        for r in f:
            print("\n",r)

# Reservar una habitación:
# para dos recién casados: en el segundo edificio, en el décimo piso, habitación 14
rooms[1][9][13] = True
            
# Verificar disponibilidad en el piso 15 del tercer edificio
vacante = 0

for room_number in range(20):
    if not rooms[2][14][room_number]:
        vacante += 1

print("El piso 15 del tercer edificio tiene", vacante, "habitaciones disponibles")

##################################################################################
# Ejercicios
##################################################################################
print("\n")
for i in range(3):
    print("#")

print("\n")
i = 0
while i <= 3 :
    i += 2
    print("-")

print("\n")
var = 1
while var < 10:
    print("*")
    var = var << 1

my_list = [3, 1, -2]
print("\n",my_list[-1])
print(my_list[my_list[-1]])

my_list = [1, 2, 3, 4]
print("\n",my_list[-3:-2])

print("\n")
vals = [0, 1, 2]
vals.insert(0, 1)
print(vals)
del vals[1]
print(vals[0]+vals[1]+vals[2])

my_list = [i for i in range(-1, 2)]
print("\n", my_list)

nums = [1, 2, 3]
vals = nums[-1:-2]
print("\n", nums)
print(vals)





