# Todos los argumentos que reciba son de forma opcional y los utilizamos para generar una tupla
def n_argumentos_tupla(*args):
    print(type(args))
    print(args)


# Todos los argumentos que reciba son de forma opcional y los utilizamos para generar un diccionario
def n_argumentos_diccionario(**kwargs):
    print(type(kwargs))
    print(kwargs)


# Combinamos los parametros requeridos, con parametros opcionales para tuplas y diccionarios y parametros por default
def combinacion(a, b, *args, enable=True, **kwargs):
    print(a, b, args, kwargs, enable, sep=' | ')


#n_argumentos_tupla({'Nombre': 'Héctor', 'Apellido': 'Mastache'}, 33, True)
#n_argumentos_diccionario(hector={'Nombre':'Héctor', 'Apellido':'Mastache'}, Karla={'Nombre':'Karla', 'Apellido':'Orduña'})
combinacion('a', 'b', 1, 2, 3, 4, 5, usuario={'Nombre': 'Héctor', 'Apellido': 'Mastache'}, enable=False)