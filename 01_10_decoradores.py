#Es necesario importar las depencendias necesarias
from datetime import date
from datetime import timedelta
from calendar import monthrange

settlement = {}

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
def settlement_optional(fee, mw_month):
    type_fee = 'CENACE'
    type_division = 'Jalisco'
    amount = fee(type_fee, type_division) * mw_month
    return amount


# GENERADORES crean variables bajo demanda
def generador_fechas(init_date,days):
    for salto in range(0,days):
        yield init_date + timedelta(days=salto)



init_date = date(2024, 5, 1)
_, days_in_month = monthrange(init_date.year, init_date.day)
new_day = generador_fechas(init_date,days_in_month)

amount = settlement_optional(function_fee, 1000)
amount_daily = amount / days_in_month

while True:
    # MANEJO DE ERRORES
    try:
        # USAMOS EL GENERADOR
        settlement.setdefault(next(new_day), amount_daily) 
    except StopIteration:
        break


print(settlement)
