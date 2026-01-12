class Cliente:
    def __init__(self,nome,idade,telefone,email):
        self.nome = nome
        self.idade = idade
        self.telefone = telefone
        self.email = email


    def __str__(self):
        return f'{self.nome} | {self.idade} | {self.telefone} | {self.email}'
    
primeiro_cliente = Cliente('Julio',25,'(51)986520067','julio_na_gaita@gmail.com')