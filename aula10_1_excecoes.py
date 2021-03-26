lista = [1, 10]
arquivo = open('aula8_2_teste.txt', 'r')
try:
    # divisao = 10 / 0      - ZeroDivisionError
    # numero = lista[3]     - IndexError
    # x = 0                 - BaseException
    texto = arquivo.read()
except ZeroDivisionError:
    print('nao pode fazer divisao por 0')
except IndexError:
    print('Erro ao acessar um dado invalido da lista')
except BaseException as ex:
    print('Erro desconhecido. Erro: {}'.format(ex))
else:
    print('executa quando nao ocorre excecao!')
finally:
    print('executa sempre!')
    arquivo.close()