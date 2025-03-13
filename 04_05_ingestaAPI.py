import requests
import pandas

if __name__ == '__main__':
    #REALIZAMOS UNA SOLICITUD GET
    response = requests.get('https://disease.sh/v3/covid-19/countries')

    data = response.json()

    for item in data:
        print(item)

    # CREAMOS UNA LISTA DE TODOS LOS PAISES QUE CONTIENE EL REQUEST
    countries = list(map(lambda item : item['country'], data))
    print(countries)

    print('*' * 30)

    # CREAMOS UNA TUPLA QUE CONTENGA EL NOMBRE DE PAIS Y SU POBLACIÓN
    tupla_population = {item['country']: item['population'] for item in data}
    print(tupla_population)

    # CREAMOS UN DATAFRAME CON LOS DATOS DEL REQUEST
    df = pandas.DataFrame(data)
    print(df.head())