################################################################
# Ejercicio lista dentro de lista 
# Tablero de ajedrez

tablero = []
estaOcupado = False

torreBlanco   = "Torre"
alfilBlanco   = "Alfil"
caballoBlanco = "Caballo"
reyBlanco     = "Rey"
reinaBlanco   = "Reina"
torreBlanco   = "Torre"
peonBlanco    = "Peón"

torreNegro   = "Torre"
alfilNegro   = "Alfil"
caballoNegro = "Caballo"
reyNegro     = "Rey"
reinaNegro   = "Reina"
torreNegro   = "Torre"
peonNegro    = "Peón"

for i in range(8):
    fila = [estaOcupado for i in range(8)]
    tablero.append(fila)

################################################################
# se puede hacer lo anterior de esta forma:

tablero2 = [[estaOcupado for i in range(8)] for j in range(8)]

################################################################
# Mostrar tableros
# El acceso al campo seleccionado del tablero requiere dos índices - 
# el primero selecciona la fila; el segundo - el número del campo dentro de la fila, 
# el cual es un número de columna.
################################################################

def mostrarTablero(tablero, tablero2): 
    print("\n###################################\n")

    print("Tablero 1: \n")
    for row in tablero:
        print(row)

    print("\nTablero 2: \n")

    for row in tablero2:
        print(row)

    print("\n###################################\n")

mostrarTablero(tablero, tablero2)

################################################################
# Agregar torres a los tableros
################################################################

tablero[0][0] = torreBlanco
tablero[0][1] = caballoBlanco
tablero[0][2] = alfilBlanco
tablero[0][3] = reyBlanco
tablero[0][4] = reinaBlanco
tablero[0][5] = caballoBlanco
tablero[0][6] = alfilBlanco
tablero[0][7] = torreBlanco
tablero[7][0] = torreNegro
tablero[7][1] = caballoNegro
tablero[7][2] = alfilNegro
tablero[7][3] = reyNegro
tablero[7][4] = reinaNegro
tablero[7][5] = caballoNegro
tablero[7][6] = alfilNegro
tablero[7][7] = torreNegro

tablero2[0][0] = torreBlanco
tablero2[0][1] = caballoBlanco
tablero2[0][2] = alfilBlanco
tablero2[0][3] = reyBlanco
tablero2[0][4] = reinaBlanco
tablero2[0][5] = caballoBlanco
tablero2[0][6] = alfilBlanco
tablero2[0][7] = torreBlanco
tablero2[7][0] = torreNegro
tablero2[7][1] = caballoNegro
tablero2[7][2] = alfilNegro
tablero2[7][3] = reyNegro
tablero2[7][4] = reinaNegro
tablero2[7][5] = caballoNegro
tablero2[7][6] = alfilNegro
tablero2[7][7] = torreNegro

mostrarTablero(tablero, tablero2)

################################################################

################################################################