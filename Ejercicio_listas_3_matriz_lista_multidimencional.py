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