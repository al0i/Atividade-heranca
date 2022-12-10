from data import Data

class Voo:
    def __init__(self,nVoo,data):
        self.nVoo = nVoo
        self.data = Data(data)
        self.horario = None
        self.bancos = list(range(1,101))
        self.nVagas = list(range(1,101))

    def proximoLivre(self):
        return self.bancos[0]
    
    def verifica(self,nBanco):
        if nBanco > self.nVagas[-1]:
            return 'Cadeira inexistente'
        elif nBanco in self.bancos:
            return 'Disponível'
        else:
            return 'Indisponível'

    def ocupa(self, nBanco):
        if nBanco in self.bancos:
            self.bancos.remove(nBanco)
            return True
        else:
            return False
        
    def vagas(self):
        return len(self.bancos)

    def getVoo(self):
        return self.nVoo
    
    def getData(self):
        return self.data
