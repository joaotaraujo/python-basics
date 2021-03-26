# calcula media bimestral ------------------------
a = int(input('Primeiro bimestre: '))
b = int(input('Segundo bimestre: '))
c = int(input('Terceiro bimestre: '))
d = int(input('Quarto bimestre: '))

media = (a + b + c + d) / 4

if a <= 10 and b <= 10 and c <= 10 and d <= 10:
    print('media: {}'.format(media))
else:
    print('foi informado alguma nota errada')


# verifica se eh par ------------------------------
a = int(input('Entre com o primeiro valor: '))
b = int(input('Entre com o segundo valor: '))
resto_a = a % 2
resto_b = b % 2

if resto_a == 0 or not resto_b != 0:
    print("um dos numeros sao pares")
else:
    print("nenhum numero par encontrado")


# verifica numero maior ----------------------------
a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))

if a > b and a > c:
    print('o maior número é {}'.format(a))
elif b > a and b > c:
    print('o maior numero é {}'.format(b))
else:
    print('o maior numero é {}'.format(c))

print('final do programa')