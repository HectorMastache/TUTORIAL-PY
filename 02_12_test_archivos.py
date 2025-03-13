import csv
import functools

def read_csv(path):
   # Tu código aquí 👇
   with open(path, 'r') as archivo:
      reader = csv.reader(archivo)
      items = {value[0]: value[1] for value in reader}
      total = functools.reduce(lambda counter, value : counter + float(value), items.values(), 0.0)
   return total

response = read_csv('02_data.csv')
print(f'\nEl RESULTADO ES: {response}')