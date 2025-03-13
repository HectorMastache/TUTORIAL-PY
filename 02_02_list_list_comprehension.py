# EJEMPLO 1 DE LISTAS CON COMPREHENSION
numbers = []
for element in range(1,11):
    numbers.append(element * 2)
print(numbers)

#COMPREHENSION
numbers_v2 = [element * 2 for element in range(1,11)]
print(numbers_v2)

# EJEMPLO 2 DE LISTAS CON COMPREHENSION
numbers = []
for element in range(1,11):
    if element % 2 == 0:
        numbers.append(element * 2)
print(numbers)

#COMPREHENSION
numbers_v2 = [element * 2 for element in range(1,11) if element % 2 == 0]
print(numbers_v2)