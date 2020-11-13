class Pessoa:
    def __init__(self, *familia, nome=None, idade=30, parentesco=None):
        self.nome = nome
        self.idade = idade
        self.familia = list(familia)
        self.parentesco = parentesco

    def cumprimentar(self):
        return f'Olá {id(self)}'


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
