class Carro:
    carros = []
    def __init__(self,modelo,cor,ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        Carro.carros.append(self)
    
    def __str__(self):
        return f'{self.modelo} | {self.cor} | {self.ano}'
    
    def listar_carros():
        for carro in Carro.carros:
            print(f'{carro.modelo.ljust(25)} | {carro.cor.ljust(25)} | {carro.ano}')
     
primeiro_carro = Carro('Toyota Corolla','Preto','2020')
segundo_carro = Carro('Ford Mustang','Vermelho','2024')
terceiro_carro = Carro('Tesla Model S','Branco','2022')

Carro.listar_carros()

    