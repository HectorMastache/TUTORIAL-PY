import json

with open('07_settlement_SAP.json', 'r') as archivo:
    datos = json.load(archivo)
try:
    if datos.get('NUMSERVSOLICITANTE'):
        print(datos.get('NUMSERVSOLICITANTE'))
    else:
        raise Exception('LA ETIQUETA NO PUEDE CONTENER CARACTERES NULOS O VACIOS')
except Exception as error:
    print(error)