

# DEFINICIÓN DE UN CICLO WHILE
print('\nDefinición de un Ciclo While')
counter = 0
while counter < 5 :
    counter += 1
    print(counter)
    
# ROMPER LA EJECUCIÓN DE UN CICLO WHILE
print('\nParo forzado de un ciclo while')
counter = 0
while counter < 5 :
    counter += 1
    if counter == 3:
        break
    print(counter)
    
# EXCLUIR ALGUANA EJECUCIÓN DE UN CICLO WHILE
print('\nExcluir una ejecución de un ciclo while')
counter = 0
while counter < 5 :
    counter += 1
    if counter == 3:
        continue
    print(counter)
    