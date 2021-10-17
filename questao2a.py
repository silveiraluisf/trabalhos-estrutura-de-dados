class Lista:

    def __init__(self, lista: list):
        self.__lista = lista
        self.__tamanho = len(self.__lista)
        self.__contador = 0
        

    def meio(self):

        for i in range(self.__tamanho):
                self.__contador += 1 

        if self.__contador % 2 is not 0:
            indice = int((self.__tamanho / 2) - 0.5)
            resposta = self.__lista[indice]

        else:
            indice = int(self.__tamanho // 2)
            resposta = self.__lista[int(indice - 1)], self.__lista[indice]

        return resposta
