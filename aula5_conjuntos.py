# operacoes
conjunto = {1, 2, 3, 4, 5}
conjunto2 = {5, 6, 7, 8}

conjunto_uniao = conjunto.union(conjunto2)  # uniao
conjunto_intersecao = conjunto.intersection(conjunto2)  # intersecao
conjunto_diferenca = conjunto.difference(conjunto2)  # diferenca
conjunto_diff_simetric = conjunto.symmetric_difference(conjunto2)  # diff simetrica


# pertinencia
conjunto_a = {1, 2, 3}
conjunto_b = {1, 2, 3, 4, 5}

conjunto_a.issubset(conjunto_b)  # subset (se um conjunto eh subconjunto de outro)
conjunto_b.issuperset(conjunto_a)  # subset (b eh superconjunto de a, pq a esta contido nele)

lista = ['cachorro', 'cachorro', 'gato', 'gato']
conjunto_animais = set(lista)
lista_animais = list(conjunto_animais)


# adicionando e removendo itens
# conjunto nao aceita itens iguais
conjunto = {1, 2, 3, 4, 4, 2}
conjunto.add(5)
conjunto.discard(2)

print(type(conjunto))
