from contextlib import nullcontext
from pydoc import doc


class Carro:
    
    def __init__(self, consumo):
        self.consumo = consumo
        self.combustivel = 0
        print('Seu carro tem um consumo médio de {} Km/L'.format(self.consumo))

    def andar(self, distancia):
        gasto = distancia / self.consumo
        
        if(self.combustivel < gasto):
            print('Você não tem gasolina para andar essa distância, abasteça!')
        else:
            self.combustivel -= gasto
            print('Você andou {} quilômetros'.format(distancia))
        


    def obterGasolina(self):
        print('O nível atual de combustível é {} litros'.format(self.combustivel))

    def adicionarGasolina(self, gasolinaAdicionada):
        self.combustivel += gasolinaAdicionada
        print('Você adicionou {} litros de gasolina'.format(gasolinaAdicionada))


carro = Carro(10)

carro.obterGasolina()

carro.andar(10)

carro.adicionarGasolina(10)

carro.obterGasolina()

carro.andar(15)

carro.obterGasolina()

