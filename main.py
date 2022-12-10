from data import Data
from voo import Voo
from vooFumante import VooFumante

if __name__ == '__main__':
    #Teste da classe Data
    print('\n------------Data------------')
    data1 = Data('22/11/2005')
    data2 = Data('13/07/2005')
    print(data1)
    print(data2)
    print(data1.compara(data2))
    print(data1.isBissexto())
    print(data2.getDia(),data2.getMesExtenso(),data2.getAno())

    #Teste da classe Voo
    print('\n------------Voo------------')
    azul = Voo('0001','12/12/2022')
    print(azul.vagas())
    print(azul.verifica(1))
    print(azul.ocupa(1))
    print(azul.proximoLivre())
    print(azul.vagas())


    #Teste da classe VooFumante
    print('\n------------VooFumante------------')
    malboro = VooFumante('1020','13/13/2023',50,15)
    print(malboro.getVoo())
    print(malboro.maxVagas())
    print(malboro.cadeirasFumantes())
    print(malboro.verifica(30))
    print(malboro.ocupa(30))
    print(malboro.ocupa(1))
    print(malboro.proximoLivre())
    print(malboro.vagas())
