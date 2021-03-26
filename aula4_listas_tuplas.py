lista = [1, 2, 3, 4]
lista_animal = ['cachorro', 'gato', 'elefante']

# triplica a lista
lista_animal = lista_animal * 3
print(lista_animal)

# pega o maior inteiro da lista
print(max(lista))

# inclui lobo/elemento na lista
if 'lobo' in lista_animal:
    print('a lista contem o animal lobo')
else:
    print('a lista nao contem o animal lobo')
    lista_animal.append('lobo')
    print(lista_animal)


# remocao de item
lista_animal.pop(1)
#lista_animal.remove('elefante')
print(lista_animal)

# ordenacao da lista
lista.sort()
print(lista)

# reverter os itens de uma lista
lista_animal.reverse()
print(lista_animal)

# criando uma tupla (lista que nao pode ser alterada)
tupla = (1, 2, 3, 4)
# tupla[0] = 100  (ERROR)
print(len(tupla))  # retorna tamanho da tupla

# convertendo lista em tupla
tupla_animal = tuple(lista_animal)

# convertendo tupla em lista
lista_numerica = list(tupla)
print(type(lista_numerica))