diccionario = {
    'name' : 'Héctor de Jesús',
    'last_name' : 'Mastache Salgado',
    'curp' : "MASH900524HGRSLC07",
    'age' : 24,
    'state' : 'Guerrero',
    'country' : 'México',
    'street' : 'Pineda',
    'house' : '47-B'
}

lista = ['Héctor', 'Mastache', 'Salgado', 33, True, [1, 2, 3, 4, 5], diccionario]

usuarios = [
    {
        'name' : 'Héctor de Jesús',
        'last_name' : 'Mastache Salgado',
        'curp' : "MASH900524HGRSLC07",
        'age' : 33
    },
    {
        'name' : 'Oliver',
        'last_name' : 'Mastache Orduña',
        'curp' : "MAOO100730HGRSLC07",
        'age' : 14
    },
    {
        'name' : 'Karla Mireya',
        'last_name' : 'Orduña Martinez',
        'curp' : "ORMK900925HGRSLC07",
        'age' : 33
    }
]



# ITERAR UN DICCIONARIO
for clave, valor in diccionario.items():
    print(f'Clave: {clave}  Valor: {valor}')

# ITERAR UNA LISTA
for elemento in lista:
    print(f'Valor: {elemento}  Tipo:{type(elemento)}')

# PRUEBAS
for usuaio in usuarios:
    nombre = usuaio.get('name')
    apellido = usuaio.get('last_name')
    edad = usuaio.get('age')
    print(f'El usuario {nombre} {apellido} dentro de 10 años tendra {edad + 10} años.')

texto = 'texto'
texto.case