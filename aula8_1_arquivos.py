import shutil

# 'w' ele reescreve o arquivo original
# 'a' ele adiciona o conteudo
def escrever_arquivo(texto):
    arquivo = open('aula8_2_teste.txt', 'w')
    # diretorio = 'C:/Projetos...'
    # arquivo = open(diretorio, 'w')
    arquivo.write(texto)
    arquivo.close()


def atualizar_arquivo(texto):
    arquivo = open('aula8_2_teste.txt', 'a')
    arquivo.write(texto)
    arquivo.close()


def ler_arquivo(nome):
    arquivo = open(nome, 'r')
    print(arquivo.read())
    arquivo.close()


def media_notas(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    aluno_nota = arquivo.read()
    aluno_nota = aluno_nota.split('\n')
    for x in aluno_nota:
        lista_notas = x.split(',')
        aluno = lista_notas[0]
        lista_notas.pop(0)
        print(aluno)
        print(lista_notas)
        media = lambda notas: sum([int(i) for i in notas]) / 4
        print(media(lista_notas))


def copia_arquivo(nome_arquivo):
    shutil.copy(nome_arquivo, './aula8_4_notas_copia.txt')


if __name__ == '__main__':
    escrever_arquivo('Primeira linha.\n')
    atualizar_arquivo('Segunda linha.\n')
    atualizar_arquivo('Terceira linha.\n')
    ler_arquivo('aula8_2_teste.txt')

    media_notas('aula8_3_notas.txt')
    copia_arquivo('aula8_3_notas.txt')