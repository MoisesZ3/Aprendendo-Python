class ContaBancaria:
    contas = []

    def __init__(self,titular,saldo):
        self._titular = titular
        self._saldo = saldo
        self._ativo = False
        ContaBancaria.contas.append(self)

    def __str__(self):
        return f'{self._titular} | {self._saldo}'
    
    @classmethod
    def listar_contas(cls):
        print(f'{'Nome do titular'.ljust(20)} | {'Saldo'}')
        for conta in cls.contas:
            print(f'{conta._titular.ljust(20)} | {conta._saldo}')

    @property
    def ativo(self):
        return 'Ativo' if self._ativo else 'Inativo'        

    def ativar_conta(self):
        self._ativo = True
        

primeirto_titular = ContaBancaria('Danilo',2.50)
segundo_titular = ContaBancaria('Arthur',0.75)

ContaBancaria.listar_contas()
print(primeirto_titular.ativo)
primeirto_titular.ativar_conta()
print(primeirto_titular.ativo)
print(primeirto_titular._titular)
