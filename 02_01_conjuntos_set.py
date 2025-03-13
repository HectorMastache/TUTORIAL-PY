set_countries = {'col', 'mex', 'bol'}
print (set_countries)
print(type(set_countries ))

size = len(set_countries) #OBTENER LA DIMENSION DEL CONJUNTO
print(f'LA DIMENSION DEL CONJUNTO ES: {size}')

contains_pe = 'pe' in set_countries #OPERACIONES CORTAS
print(f'LA CADENA pe ESTA CONTENIDA EN EL CONJUNTO: {contains_pe}')

set_countries.add('pe') #AGREGAR VALORES INDIVIDUALES A UN CONJUNTO
print(f'LA CADENA pe ESTA CONTENIDA EN EL CONJUNTO: {'pe' in set_countries}')

set_countries.update({'arg', 'chi', 'usa', 'mex'}) #AGREGAR UN CONJUNTO DE VALORES A UN CONJUNTO YA EXISTENTE
print(set_countries) #NOTESE QUE LOS VALORES REPETIDOS SE ELIMINAR

set_countries.remove('pe') #ELIMINAR VALORES INDIVIDUALES DE UN CONJUNTO
print(set_countries)
set_countries.discard('pe') #ELIMINAR VALORES INDIVIDUALES DE UN CONJUNTO PERO CONTROLANDO EL ERROR EN CASO DE QUE NO EXISTA
print(set_countries)

set_countries.clear() #ELIMINAR EL CONJUNTO EN SU TOTALIDAD
print(set_countries)

set_a = {'a', 'b', 'c', 'd', 'e'}
set_b = {'d', 'e', 'f', 'g', 'h'}

set_c = set_a.union(set_b) #UNION DE DOS CONJUNTOS
print(f'LA UNION ENTRE DOS CONJUNTOS ES: {set_c}')
print(f'LA UNION CON EL OPERADOR | ES: {set_a | set_b}') #OTRA MANERA DE UNIR CONJUNTOS

set_c = set_a.intersection(set_b)
print(f'LA INTERSECCION ENTRE DOS CONJUNTOS ES: {set_c}')
print(f'LA INTERSECCION CON EL OPERADOR & ES: {set_a & set_b}')

set_c = set_a.difference(set_b)
print(f'LA DIFERENCIA ENTRE EL CONJUNTO A Y EL CONJUNTO B ES: {set_c}')
print(f'LA DIFERENCIA CON EL OPERADOR - ES: {set_a - set_b}')

set_c = set_a.symmetric_difference(set_b)
print(f'LA DIFERENCIA SIMETRICA ENTRE CONJUNTOS ES: {set_c}')
print(f'LA DIFERENCIA SIMETRICA CON EL OPERADOR ^ ES: {set_a ^ set_b}')

#########################################################################################################

countries = {"MX", "COL", "ARG", "USA"}
northAm = {"USA", "CANADA"}
centralAm = {"MX", "GT", "BZ"}
southAm = {"COL", "BZ", "ARG"}

new_set = countries | northAm | centralAm | southAm
print(new_set)