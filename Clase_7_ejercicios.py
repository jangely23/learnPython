# 3.2.14   LAB   Fundamentos del bucle while
# Determinar cuantos pisos puede tener una
# piramide segun la cantidad de bloques pasados

blocks = int(input("Ingresa el número de bloques: "))

height = 0
block_use = 0

while blocks > block_use :
 
    block_use += 1    
    blocks -= block_use
    height += 1
    
    
print("La altura de la pirámide:", height)


# 3.2.15   LAB   La hipótesis de Collatz
# 1- toma cualquier número entero que no sea negativo y que no sea cero y asígnale el nombre c0;
# 2- si es par, evalúa un nuevo c0 como c0 ÷ 2;
# 3- de lo contrario, si es impar, evalúe un nuevo  c0  como 3 × c0 + 1;
# 4- si c0 ≠ 1, salta al punto 2.

c0 = int(input("Digite un numero: "))

step = 0

while c0 > 1:
    
    if c0 % 2 == 0:
        c0 //= 2
    else :
        c0 = 3 * c0 + 1
    
    step += 1
    print(c0)     

print("pasos = ", step)
