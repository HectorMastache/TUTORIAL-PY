import random

def ordenamientoDeBurbuja(list):
    n = len(list)
    for i in range(n):
        for j in range(n-i-1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
    return list


if __name__ == '__main__':
    len_list = int(input('Que dimension quieres que tenga la lista?'))
    list = [random.randint(0,100) for i in range(len_list)]

    print(list)
    sort_list = ordenamientoDeBurbuja(list)
    print(sort_list)