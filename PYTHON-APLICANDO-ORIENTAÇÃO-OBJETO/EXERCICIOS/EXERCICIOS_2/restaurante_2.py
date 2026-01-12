class Restaurante_2:
    restaurantes = []

    def __init__(self,nome, categoria,capacidade,avaliacao):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        self.capacidade = capacidade
        self.avaliacao = avaliacao 
        Restaurante_2.restaurantes.append(self)

    def __str__(self):
        return f'{self.nome} | {self.categoria} | {self.ativo} | {self.capacidade} | {self.avaliacao}'
    
    def listar_restaurantes():
        for restaurante in Restaurante_2.restaurantes:
            print(f'{restaurante.nome.ljust(25)} | {restaurante.categoria.ljust(25)} | {restaurante.ativo} | {restaurante.capacidade} | {restaurante.avaliacao}')

restaurante_praca = Restaurante_2('Praça','Gourmet', 50, 9.8)
restaurante_pizza = Restaurante_2('Pizza Express','Italiana', 40, 7.9)

Restaurante_2.listar_restaurantes()
