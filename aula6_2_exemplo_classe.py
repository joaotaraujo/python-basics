class Calculadora:
    def __init__(self, a, b):
        pass

    def soma(self, a, b):
        return a + b

    def subtracao(self, a, b):
        return a - b

    def multiplicacao(self, a, b):
        return a * b

    def divisao(self, a, b):
        return a / b


calculadora = Calculadora(10, 2)
print(calculadora.soma(10, 2))
print(calculadora.subtracao(10, 2))
print(calculadora.multiplicacao(10, 2))
print(calculadora.divisao(10, 2))
