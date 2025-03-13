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

# FUNCION LAMBDA 
function_fee = lambda tarifa, division : fee_divisional.get(tarifa).get(division)


# CALLBACKS Es cuando se le pasa una 'funcion' como parametro a otra funcion
def settlemnet_optional(fee, mw_month):
    type_fee = 'CENACE'
    type_division = 'Jalisco'
    amount = fee(type_fee, type_division) * mw_month
    print(f'El consumo mensual  {mw_month} y el monto: {amount}')

#type_fee = 'CENACE'
#type_division = 'Jalisco'
#tarifa = function_fee(type_fee, type_division)
#print(f'La tarifa de {type_fee} para la division {type_division} es: {tarifa}')

settlemnet_optional(function_fee, 1000)