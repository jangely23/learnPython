my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9, 1, 20, 4, 2, 5, 6, 2, 3, 9, 8, 2]
new_list = []
cambio = True

while cambio:
    cambio = False

    for i in range(len(my_list)):

        if len(new_list) == 0:
            new_list.append(my_list[i])

        elif my_list[i] in new_list:
            cambio = True
            del my_list[i]
            break
        else:
            new_list.append(my_list[i])

    new_list = []

print("La lista con elementos únicos:")
print(my_list)