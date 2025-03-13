import random

def busquedaLineal(list, value):
    match = False
    for item in list:
        if item == value:
            match = True
            break
    return match

if __name__ == '__main__':
    leng_list = int(input('Que tamano tiene la lista?'))
    value = int(input('Que numero quieres encontrar?'))
    list = [random.randint(0,100) for i  in range(leng_list)]

    find = busquedaLineal(list, value)

    print(list)
    print(f'El elemento {value} {'se encuentra' if find else 'No esta'} en la lista')