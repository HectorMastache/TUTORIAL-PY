import csv

def read_csv(path):
    with open(path, 'r') as archivo:
        reader = csv.reader(archivo, delimiter=',')
        headers = next(reader)
        data = []

        for row in reader:
            iterable = zip(headers,row)
            item = {key: value for key, value in iterable}
            data.append(item)
        return data


if __name__ == '__main__':
    data = read_csv('02_11_archivos_csv.csv')
    print(data[0])