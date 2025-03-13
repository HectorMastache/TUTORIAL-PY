import random

def ordenamientoPorInsercion(list):
    for indice in range(1,len(list)):
        aux = list[indice]
        position = indice

        while position > 0 and list[position-1] > aux:
            list[position] = list[position - 1]
            position-=1
        list[position] = aux
    return list 



if __name__ == '__main__':
    len_list = int(input('De que dimension necesitas hacer la lista?'))
    list = [random.randint(0,100) for i in range(len_list)]

    print(list)
    sort_list = ordenamientoPorInsercion(list)
    print(sort_list)