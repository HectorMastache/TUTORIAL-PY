# DEFINICION DE UN DICCIONARIO CLAVE : VALOR
person = {
    'name' : 'Héctor de Jesús',
    'last_name' : 'Mastache Salgado',
    'curp' : "MASH900524HGRSLC07",
    'age' : 24,
    'state' : 'Guerrero',
    'country' : 'México',
    'street' : 'Pineda',
    'house' : '47-B'
}

print(person)

# OBTENER UN ELEMENTO EN ESPECIFICO
one_element =  person.get('name')
print(f'Un elemento que si existe: {one_element}')
other_element =  person.get('exist')
print(f'Otro elemento que no existe: {other_element}')

# EDICIÓN DE UN ELEMENTO QUE CONTIENE EL DICCIONARIO
person['age'] += 9
print(person)

# AGREGAR UN ELEMENTO AL DICCIONARIO
person['rfc'] = 'MASH900524L3A'
person.setdefault('add')
person.setdefault('test',True)
print(person)

# ELIMINAR ELEMENTOS DE UN DICCIONARIO
del person['test']
print(person)
# ALTERNATIVA PARA ELIMINAR ELEMENTOS DE UN DICCIONARIO
person.pop('add')
print(person)

# OBTENER ITEMS DE UN DICCIONARIO
elementos = person.items()
for elemento in elementos:
    print(f'Elemento: {elemento} Type: {type(elemento)}')

# OBTENER KEYS DE UN DICCIONARIO
llaves = person.keys()
for llave in llaves:
    print(f'Llave: {llave} Type: {type(llave)}')

# OBTENER VALORES DE UN DICCIONARIO
valores = person.values()
for valor in valores:
    print(f'Valor: {valor} Type: {type(valor)}')

# INICIALIZAR LOS ELEMENTOS CON VALORES VACIOS POR DEFAULT
person.fromkeys(person)
print(person)