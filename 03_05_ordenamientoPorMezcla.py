import random

def ordenamientoPorMezcla(list):
    if len(list) > 1:
        halft = len(list) // 2
        left = list[:halft]
        rigth = list[halft:]
        print(left, '*'*5, rigth)

        ordenamientoPorMezcla(left)
        ordenamientoPorMezcla(rigth)

        i, j, k = 0,0,0

        while i < len(left) and j < len(rigth):
            if left[i] < rigth[j]:
                list[k] = left[i]
                i+=1
            else:
                list[k] = rigth[j]
                j+=1
            k+=1
        
        while i < len(left):
            list[k] = left[i]
            i+=1
            k+=1

        while j < len(rigth):
            list[k] = rigth[j]
            j+=1
            k+=1
        
        print(f'left {left} *** rigth {rigth}')
        print(list)
        print('*' * 10)

    return list


if __name__ == '__main__':
    len_list = int(input('QUE DIMENSION NECESITAS PARA LA LISTA?'))
    list = [random.randint(0,100) for i in range(len_list)]

    print(list)
    print('-' * 20)

    sort_list = ordenamientoPorMezcla(list)