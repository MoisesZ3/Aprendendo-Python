import random

class ClienteBanco:
    clientes = []

    def __init__(self,nome,idade,email,telefone):
        self.nome = nome
        self.idade = idade
        self.email = email
        self.telefone = telefone
        self._id = random.randint(1000000000, 9999999999)
        ClienteBanco.clientes.append(self)

    def __str__(self):
        return f'{self.nome} | {self.idade} | {self.email} | {self.telefone} | {self._id}'
    
    @classmethod
    def listar_clientes(cls):
        print(f'{'Nome do titular'.ljust(20)} | {'Idade'.ljust(20)} | {'ID'}')
        for cliente in cls.clientes:
            print(f'{cliente.nome.ljust(20)} | {str(cliente.idade).ljust(20)} | {cliente._id}')

primeiro_cliente = ClienteBanco('Moisés',20,'moises@gmail.com','(51)9 86800740')
segundo_cliente = ClienteBanco('Danilo',19,'danilo.com@gmail.com','(51)9 81672000')
terceiro_cliente = ClienteBanco('Roberto',35,'rodrigo@gmail.com','(51)9 82152199')

ClienteBanco.listar_clientes()


