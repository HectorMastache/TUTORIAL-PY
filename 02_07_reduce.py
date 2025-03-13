import functools
import json

numbers = [1, 3, 5, 7, 11, 13]

def calcularTotal(counter, item):
    return counter + float(item['TOTAL'])

#EXPLICACION DEL METODO REDUCE
def methodAccum(counter, item):
    print(f'EL CONTADOR ESTA EN: {counter}')
    print(f'EL ITEM QUE ITERAMOS ES: {item}')
    return counter + item


result = functools.reduce(lambda counter, item: counter + item, numbers)
print(result)

#EJECUCIÓN CON METODO
result_v2 = functools.reduce(methodAccum,numbers)
print(f'LA EJECUCION POR METODO DA COMO RESULTADO: {result_v2}')



with open('07_settlement_SAP.json', 'r') as archivo:
    datos = json.load(archivo)

montos = datos['REQ_TAB_CONCEPTO_USD']
result = functools.reduce(lambda counter, item: counter + float(item['TOTAL']), montos, 0.0)
print(f'EL MONTO TOTAL POR MEDIO DE LAMBDA ES: {result}')

result_v2 = functools.reduce(calcularTotal,montos,0.0)
print(f'EL MONTO TOTAL POR MEDIO DEL METODO ES: {result_v2}')