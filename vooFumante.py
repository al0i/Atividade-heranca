from voo import Voo
    
class VooFumante(Voo):
    def __init__(self, nVoo, Data, bancos, nFumantes):
        super().__init__(nVoo, Data)
        self.bancos = list(range(1,int(bancos)+1))
        self.nVagas = list(range(1,int(bancos)+1))
        self.nFumantes = list(range(int(bancos)-int(nFumantes)+1,int(bancos)+1))

    def maxVagas(self):
        return len(self.bancos)

    def cadeirasFumantes(self):
        return self.nFumantes
    
    def tipo(self,nBanco):
        if nBanco in self.nFumantes:
            return 'F'
        else:
            return 'N'
        
    def proximoLivre(self):
        return super().proximoLivre(), self.tipo(self.bancos[0])

    def verifica(self, nBanco):
        return super().verifica(nBanco), self.tipo(nBanco)