# GENERADOR SERIE DE FIBONACCI
def fibonacci(limite):
    a, b = 0, 1
    while a < limite:
        yield a
        a, b = b, a + b


print()
'''
for num in fibonacci(10):
    print(num)
'''

siguiente_valor = fibonacci(20)
print(next(siguiente_valor))
print(''' PUEDE HABER MULTIPLES LINEAS ENTRE CADA VALOR
EJECUTAR MAS ACCIONES ANTES DE RETOMAR LA SIGUIENTE EJECUCIÓN''')
print(next(siguiente_valor))
print(''' PUEDE HABER MULTIPLES LINEAS ENTRE CADA VALOR
EJECUTAR MAS ACCIONES ANTES DE RETOMAR LA SIGUIENTE EJECUCIÓN''')
print(next(siguiente_valor))
print(''' PUEDE HABER MULTIPLES LINEAS ENTRE CADA VALOR
EJECUTAR MAS ACCIONES ANTES DE RETOMAR LA SIGUIENTE EJECUCIÓN''')
print(next(siguiente_valor))