import json

with open('06_filter_dict.json', 'r') as archivo:
    datos = json.load(archivo)

# Muestra el contenido cargado
#print(datos)
#print(type(datos))

#print(datos['data'][0]['HENKELSAN']['Suministro'])
data = datos['data'][0]['HENKELSAN']['Suministro']

all_concept = list(map(lambda element : element['Metodo'] , data.values()))
print(all_concept)

by_ene_neto = list(filter(lambda key : data[key]['Consumo_Tarifa'] == 'EneNeto_MWh', data.keys()))
print(by_ene_neto)


def filter_by_length(words):
   return list(filter(lambda element: len(element) > 3, words))

def comprehension(words):
    return {element for element in words if len(element) > 3}

def methodWords(word):
    if len(word) > 3:
        return word

words = ['amor', 'sol', 'piedra', 'día']

response = filter_by_length(words)
print(f'UTILIZANDO LO APRENDIDO EN FILTER OBTENEMOS: {response}')

response_v2 = comprehension(words)
print(f'UTILIZANDO LO APRENDIDO EN COMPREHENSION OBTENEMOS: {response_v2}')

response_v3 = list(filter(methodWords, words))
print(f'UTILIZANDO LO APRENDIDO EN METODOS OBTENEMOS: {response_v3}')