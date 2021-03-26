# validar uma nota
nota = int(input('Entre com uma nota: '))

while nota > 10:
    print('Nota invalida, entre com uma nota menor que 10.')
    nota = int(input('Entre com a nova nota: '))
print('Nota validada.')

# verificar numeros primos de ate o numero dado
valor = int(input('Entre com um valor: '))

for num in range(valor):
    div = 0
    for x in range(1, num + 1):
        resto = num % x
        if resto == 0:
            div += 1

    if div == 2:
        print('o numero {} eh primo'.format(num))
