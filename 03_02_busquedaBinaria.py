import random

def busquedaBinaria(list, value, init, end):

    print(f'Buscando el valor {value} en el rango {init} - {end}')

    if init > end:
        return False

    halft = (init + end) // 2
    if list[halft] == value:
        return True
    elif list[halft] > value:
        return busquedaBinaria(list, value, init, halft -1)
    else:
        return busquedaBinaria(list, value, halft + 1, end)

if __name__ == '__main__':
    leng_list = int(input('Cuantos Elementos Quieres que Contenga la Lista?'))
    value = int(input('Que elemento necesitas encontrar?'))

    list = sorted([random.randint(0,100) for i in range(leng_list)])

    find = busquedaBinaria(list, value, 0, len(list))

    print(f'El valor {value} {'se encuentra' if find else 'No esta'}')