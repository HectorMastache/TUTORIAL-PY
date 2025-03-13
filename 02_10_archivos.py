
# ESTE MODULO SOLO DEJA LEER EL ARCHIVO Y EN AUTOMATICO LIBERA LA MEMORIA CUNADO SE DEJA DE UTILIZAR
with open('07_settlement_SAP.json', 'r') as archivo:
    for line in archivo:
        print(line)

# EL SIGUIENTE MODULO DEJA LEER Y AGREGAR TEXTO EN EL ARCHIVO. EN AUTOMATICO LIBERA LA MEMORIA CUNADO SE DEJA DE UTILIZAR
with open('10_archivo.txt', 'r+') as archivo:
    for line in archivo:
        print(line)
    
    #AGREGAMOS TEXTO
    archivo.write("\nNUEVA LINEA CREADA DESDE EL ARCHIVO 10_archivo.py")

# EL SIGUIENTE MODULO DEJA LEER Y REMPLAZA EL TEXTO EN EL ARCHIVO. EN AUTOMATICO LIBERA LA MEMORIA CUNADO SE DEJA DE UTILIZAR
with open('10_archivo2.txt', 'w+') as archivo:
    for line in archivo:
        print(line)
    
    #REMPLAZAMOS TEXTO
    archivo.write("\nNUEVA LINEA CREADA DESDE EL ARCHIVO 10_archivo.py")