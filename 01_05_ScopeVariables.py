#COMPROBAMOS COMO PYTHON PUEDE DIFERENCIAR DE UNA VARIABLE GLOBAL Y UNA LOCAL

fee_divisional = {  #VARIABLE GLOBAL
    'CENACE':{
        'Bajio':1,
        'CentroOccidente':2,
        'CentroOriente':3,
        'CentroSur':4,
        'Jalisco':5
    },
    'Capacidad':{
        'Bajio':1,
        'CentroOccidente':2,
        'CentroOriente':3,
        'CentroSur':4,
        'Jalisco':5
    }
}


# VARIABLES LOCALES Pueden tener el mismo nombre que las variables globales, python diferencia entre ellas
def manipulacion_variable_local():
    fee_divisional = 'Héctor de Jesús Mastache Salgado'  #VARIABLE LOCAL
    print('Variable Local')
    print(fee_divisional)
    print(id(fee_divisional))


# VARIABLES GLOBALES Para maniputar estas variables es necesario definirlas con la palabra reservada "global"
def manipulacion_variable_global():
    global fee_divisional
    fee_divisional = {  # EDICION DE UNA VARIABLE GLOBAL
        'Generacion':{
            'Bajio':1,
            'CentroOccidente':2,
            'CentroOriente':3,
            'CentroSur':4,
            'Jalisco':5
        }
    }

    print('Variable Global Manipulada')
    print(fee_divisional)
    print(id(fee_divisional))


# VARIABLES NO LOCALES Son variables que viven un nivel mas alto
def variable_no_local():
    variable_local = "Karla Mireya" #VARIABLE LOCAL
    print('Variable Local')
    print(variable_local)
    print(id(variable_local))

    # FUNCION ANIDADA
    def manipulacion_variable_no_local():
        nonlocal variable_local # VARIABLE NO LOCAL
        variable_local += ' Orduña Martinez'

    manipulacion_variable_no_local()
    print('Variable Local')
    print(variable_local)
    print(id(variable_local))


print()
print('Variable Global')
print(fee_divisional)
print(id(fee_divisional))
manipulacion_variable_local()
print()
manipulacion_variable_global()
print()
variable_no_local()
