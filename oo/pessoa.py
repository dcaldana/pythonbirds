class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá, meu nome é {self.nome}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'

class Homem(Pessoa):
    def cumprimentar(self):
        cumprimentar_da_classe = super().cumprimentar()
        return f'{cumprimentar_da_classe}. *aperto de mão*'

class Mutante(Pessoa):
    olhos = 3
    pass

if __name__ == '__main__':
    daniel = Mutante(nome='Daniel')
    luciano = Homem(daniel, nome='Luciano')
    print(Homem.cumprimentar(luciano))
    print(id(luciano))
    print(luciano.cumprimentar())
    print(luciano.nome)
    print(luciano.idade)
    for filho in luciano.filhos:
        print(filho.nome)
    luciano.sobrenome='Costa'
    del luciano.filhos
    luciano.olhos=1
    del luciano.olhos
    print(luciano.__dict__)
    print(daniel.__dict__)
    print(Pessoa.olhos)
    print(luciano.olhos)
    print(daniel.olhos)
    print(id(Pessoa.olhos), id(luciano.olhos), id(daniel.olhos))
    print(Pessoa.nome_e_atributos_de_classe(), luciano.nome_e_atributos_de_classe())
    pessoa=Pessoa('Anonimo')
    print(isinstance(pessoa, Pessoa))
    print(isinstance(pessoa, Homem))
    print(isinstance(daniel, Pessoa))
    print(isinstance(daniel, Homem))
    print(daniel.olhos)
    print(luciano.cumprimentar())
    print(daniel.cumprimentar())