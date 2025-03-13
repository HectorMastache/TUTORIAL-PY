import random

items = [
    {
        'concept' : 'ENERGIA CONTRATADA',
        'nomenclature' : 'eneContr',
        'position' : 10
    },
    {
        'concept' : 'ENERGIA MEM',
        'nomenclature' : 'eneContr',
        'position' : 20
    },
    {
        'concept' : 'ENERGIA VENDIDA',
        'nomenclature' : 'eneContr',
        'position' : 30
    },
    {
        'concept' : 'ENERGIA ABASTO AISLADO',
        'nomenclature' : 'eneContr',
        'position' : 40,
    }
]

def addAmount(item):
    item['amount'] = random.randint(1000,10000)
    return item

conceptLiq = list(map(lambda item : item['concept'], items))
print(conceptLiq)

new_dict = list(map(addAmount, items))
print(new_dict)