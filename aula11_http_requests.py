import requests


def retorna_cep(cep):
    response = requests.get('https://viacep.com.br/ws/{}/json'.format(cep))
    print(response.status_code)
    dados_json = response.json()
    print(dados_json['cep'])
    return dados_json


def retorna_dados_pokemon(nome):
    response = requests.get('https://pokeapi.co/api/v2/pokemon/{}/'.format(nome))
    dados_pokemon = response.json()
    return dados_pokemon


def retorna_response(url):
    response = requests.get(url)
    return response.text


if __name__ == '__main__':
    retorna_cep('22041001')

    print(retorna_dados_pokemon('pikachu')['sprites']['front_shiny'])

    print(retorna_response('https://g1.globo.com/'))