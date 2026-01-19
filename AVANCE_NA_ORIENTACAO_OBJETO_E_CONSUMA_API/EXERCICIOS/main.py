from exercicios_1_2.carro import Carro
from exercicios_1_2.moto import Moto

carro_1 = Carro('Fiat','Mob',4)
carro_2 = Carro('Hyundai','Veloster',3) 
carro_3 = Carro('Jeep','Wrangler',2)

moto_1 = Moto('Kawasaki','Ninja ZX-10R','Esportiva')
moto_2 = Moto('Yamaha','YZF-R15','Esportiva')
moto_3 = Moto('Royal Enfield','Classic 350','Casual')

def __main__():
    print(carro_1)
    print(carro_2)
    print(carro_3)

    print(moto_1)
    print(moto_2)
    print(moto_3)
    
if __name__ == '__main__':
    __main__()