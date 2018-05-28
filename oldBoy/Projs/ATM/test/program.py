
# author: elan

dict1 = {
    'name':'elan',
    'age':22
}

dict2 = {
    'name':'elan1',
    'age':23
}

lista = [dict1, dict2]

print(lista)

# select
date = [ item for item in lista if item.get('name') == 'elan2' ]

#print([ item.get('age') for item in lista if item.get('name') == 'elan2' ])

# insert
dict3 = {
    'name':'elan2',
    'age':23
}
lista.append(dict3)
print(lista)

# update
for i in range(len(lista)):
    if lista[i].get('name') == 'elan2' :
        lista[i]['age'] = 32




