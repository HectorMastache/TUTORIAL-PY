import random

# EJEMPLO 1 DE DICCIONARIOS CON COMPREHENSION
dict = {}
for element in range(1,11):
    dict[element] = element * 2
print(dict)

#COMPREHENSION
dict_v2 = {element : element * 2 for element in range(1,11)}
print(dict_v2)

# EJEMPLO 2 DE DICCIONARIOS CON COMPREHENSION
countries = ['col', 'mex', 'arg']
population = {}
for country in countries:
    population[country] = random.randint(1,100)
print(population)

#COMPREHENSION
population_v2 = {}
population_v2 = {country : random.randint(1,100) for country in countries}
print(population_v2)

names = ['Hector', 'Karla', 'Oli']
ages = [34, 33, 14]


# EJEMPLO 3 DE DICCIONARIOS CON COMPREHENSION
users = {name : age for (name, age) in zip(names, ages)}
print(users)

# EJEMPLO 4 DE DICCIONARIOS CON COMPREHENSION
population_bigger = {contry: populat for (contry, populat) in population_v2.items() if populat > 50}
print(population_bigger)

# EJEMPLO 4 DE DICCIONARIOS CON COMPREHENSION
text = "Hola mundo, cruel y despiadado"
vocal = {c : c.upper() for c in text if c in 'aeiou'}
print(vocal)