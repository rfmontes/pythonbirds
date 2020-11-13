class Pessoa:
    olhos = 2  # como esse é um valor comum entre pessoas ele pode ser definido como atributo de classe

    def __init__(self, *familia, nome=None, idade=30, parentesco=None):
        self.nome = nome
        self.idade = idade
        self.familia = list(familia)
        self.parentesco = parentesco

    def cumprimentar(self):
        return f'Olá {id(self)}'

    @staticmethod
    def metodo_estatico():
        return 'Sou um metodo estatico'

    @classmethod
    def nome_e_atributos_de_clase(cls):
        return f'{cls} - olhos {cls.olhos}'


if __name__ == '__main__':
    alice = Pessoa(nome='Alice', idade=2, parentesco='filha')
    bella = Pessoa(nome='Bella', idade=0, parentesco='filha')
    angelica = Pessoa(nome='Angelica', idade=28, parentesco='Esposa')
    rafael = Pessoa(alice, bella, angelica, nome='Rafael', idade=28, parentesco='Pai')
    print(Pessoa.cumprimentar(rafael))
    print(id(rafael))
    print(rafael.cumprimentar())
    print(rafael.nome, rafael.idade, rafael.parentesco)
    for familia in rafael.familia:
        print(familia.nome, familia.idade, familia.parentesco)
    rafael.sobrenome = 'Fernandes'
    print(rafael.nome, rafael.sobrenome)
    print(rafael.__dict__)
    print(angelica.__dict__)
    del rafael.sobrenome
    print(rafael.__dict__)
    print(angelica.__dict__)
    print(angelica.olhos)
    print(rafael.olhos)
    rafael.olhos = 1
    print(angelica.olhos)
    print(rafael.olhos)
    print(id(angelica.olhos), id(angelica.olhos), id(Pessoa.olhos))
    del rafael.olhos
    print(angelica.olhos)
    print(rafael.olhos)
    print(id(angelica.olhos), id(angelica.olhos), id(Pessoa.olhos))
    print(Pessoa.metodo_estatico(), rafael.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_clase(), rafael.nome_e_atributos_de_clase())

