from aula6_3_classe_com_main import Televisao
from aula7_2_contador_palavras import contador_letras

if __name__ == '__main__':
    televisao = Televisao()
    televisao.power()
    print(televisao.ligada)

    lista = ['morcego', 'gaivota']
    print(contador_letras(lista))


