from exercicios_1_2.veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self,marca,modelo,portas):
        super().__init__(marca,modelo)
        self._portas = portas

    def __str__(self):
        return f'{self._marca} | {self._modelo} | {self._portas} | {self._ligado}'
    
    def ligar(self):
        return super().ligar()