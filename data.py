class Data:
    def __init__(self,data):
        self.data = self.verifica(data)
        self.dma = self.data.split('/')

    def verifica(self,data):
        dataf = data.split('/')
        if int(dataf[0]) < 1 or int(dataf[0]) > 31:
            dataf[0] = '01'
        if int(dataf[1]) < 1 or int(dataf[1]) > 12:
            dataf[1] = '01'
        if int(dataf[2]) < 1:
            dataf[2] = '0001'
        return f"{dataf[0]}/{dataf[1]}/{dataf[2]}"

    def compara(self,Data):
        if int(self.dma[2]) == int(Data.dma[2]) and int(self.dma[1]) == int(Data.dma[1]) and int(self.dma[0]) == int(Data.dma[0]):
            return 0
        elif int(Data.dma[2]) > int(self.dma[2]):
            return -1
        elif int(Data.dma[2]) < int(self.dma[2]):
            return 1
        elif int(Data.dma[2]) == int(self.dma[2]):
            if int(Data.dma[1]) > int(self.dma[1]):
                return -1
            elif int(Data.dma[1]) < int(self.dma[1]):
                return 1
            elif int(Data.dma[1]) == int(self.dma[1]):
                if int(Data.dma[0]) > int(self.dma[0]):
                    return -1
                elif int(Data.dma[0]) < int(self.dma[0]):
                    return 1

    def getDia(self):
        self.dma = self.data.split('/')
        return self.dma[0]

    def getMes(self):
        self.dma = self.data.split('/')
        return self.dma[1]

    def getMesExtenso(self):
        meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
        self.dma = self.data.split('/')
        return meses[int(self.dma[1])-1]
    
    def getAno(self):
        self.dma = self.data.split('/')
        return self.dma[2]

    def isBissexto(self):
        self.dma = self.data.split('/')
        if (int(self.dma[2]) % 4 == 0 and int(self.dma[2]) % 100 != 0) or (int(self.dma[2]) % 400 == 0):
            return True
        else:
            return False
        
    def __str__(self):
        return self.data
