
#CRIACAO DA CLASSE ELEMENTO. OBJETOS DA CLASSE ELEMENTO SERÃO INSERIDOS NA LISTA
class Elemento: 

    def __init__(self, chave: int):
        self.__anterior: Elemento = None 
        self.__proximo: Elemento = None 
        self.__chave: chave

    @property
    def chave(self) -> int:
        return self.__chave

    @property
    def anterior(self):
        return self.__anterior

    @property
    def proximo(self):
        return self.__proximo

    @anterior.setter
    def anterior(self, next):
        self.__anterior = next

    @proximo.setter
    def proximo(self, next):
        self.__proximo = next


#CRIACAO DA CLASSE LISTA E TODOS OS METODOS DE BUSCA, INSERCAO E EXCLUSAO
class Lista:
    def __init__(self):
        self.__primeiro: Elemento = None
        self.__ultimo: Elemento = None
        self.__atual: Elemento = None 

    
#METODOS PRIVADOS DE CONTROLE DO CURSOR
    def __retornar_atual(self):
        return self.__atual  

    def __mover_primeiro(self):
        self.__atual = self.__primeiro
        return self.__atual

    def __mover_ultimo(self):
        if self.__primeiro is None:
            return None

        self.__atual = self.__ultimo 
        return self.__atual

    def __avancar(self, indice):
        if self.__primeiro is None:
            return None

        else: 
            p = 0
            while p != indice -1 and self.__atual.proximo != None:
                self.__atual = self.atual.proximo
                p = p + 1 

            return self.__atual 

    def __voltar(self, indice):
        if self.__atual is None:
            return None

        else: 
            p = 0
            while p != indice -1 and self.__atual.anterior != None:
                self.__atual = self.__atual.anterior
                p = p - 1 

                return self.__atual


#METODOS PUBLICOS DE ALTERAÇÃO E BUSCA DOS ELEMENTOS DA LISTA

#METODO PARA BUSCAR UM DOS ELEMENTOS DA LISTA
    def buscar(self, chave, reiniciar=False):
        ex_atual = self.__atual

        if self.__atual is None:
            return False

        self.__mover_primeiro()
        while self.__atual.chave != chave and self.__atual.proximo != None:
            self.__atual = self.__atual.proximo

        if self.__atual.chave == chave:
            if reiniciar == True:
                self.__atual = ex_atual
            return True
        else:
            if reiniciar == True:
                self.__atual = ex_atual
            return False

#METODOS PARA INSERCAO DE ELEMENTOS DENTRO DA LISTA
    def inserir_primeiro(self, elemento: int):

        novo_elemento = Elemento(elemento)
        primeiro = self.__mover_primeiro()

        if primeiro is not None:
            primeiro.anterior = novo_elemento
            novo_elemento.proximo = primeiro
            primeiro = novo_elemento
        else:
            primeiro = novo_elemento
            self.__ultimo = primeiro

        self.__primeiro = novo_elemento
        self.__atual = novo_elemento

    def inserir_proximo_atual(self, elemento: int):

        if self.__atual is None:
            self.inserir_primeiro(elemento)
        else:
            novo_elemento = Elemento(elemento)

            if self.__atual.proximo is None:
                novo_elemento.anterior = self.__atual
                self.__atual.proximo = novo_elemento
                self.__ultimo = novo_elemento
            else:
                novo_elemento.proximo = self.__atual.proximo
                self.__atual.proximo.anterior = novo_elemento
                novo_elemento.anterior = self.__atual
                self.__atual.proximo = novo_elemento

            self.__atual = novo_elemento

    def inserir_antes(self, elemento: int): 

        if self.__atual is None:
            self.inserir_proximo_atual(elemento)
        else:
            novo_elemento = Elemento(elemento)

            if self.__atual.anterior is None:
                novo_elemento.proximo = self.__atual
                self.__atual.anterior = novo_elemento

                if self.__atual == self.__primeiro:
                    self.__primeiro = novo_elemento
            else:
                novo_elemento.anterior = self.__atual.anterior
                novo_elemento.proximo = self.__atual
                self.__atual.anterior.proximo = novo_elemento
                self.__atual.anterior = novo_elemento

            self.__atual = novo_elemento

    def inserir_ultimo(self, elemento: int):

        ultimo_elemento = self.__mover_ultimo()
        novo_elemento = Elemento(elemento)

        if ultimo_elemento is None:
            self.inserir_antes(elemento)
        else:
            ultimo_elemento.proximo = novo_elemento
            novo_elemento.anterior = ultimo_elemento

        self.__atual = novo_elemento
        self.__ultimo = self.__atual

    def inserir_na_posicao(self, indice, item):
        self.__mover_primeiro()
        self.__avancar(indice - 1)
        self.inserir_proximo_atual(item)

#METODOS PARA EXCLUSÃO DE ELEMENTOS DA LISTA
    def deletar_primeiro(self):

            self.__primeiro = self.__primeiro.proximo
            self.__primeiro.__anterior = None
            self.__atual = self.__primeiro

    def deletar_ultimo(self):
        self.__mover_ultimo()
        if self.__mover_ultimo() is not None:
            self.__atual = self.__atual.anterior
            self.__atual.proximo = None
            self.__ultimo = self.__atual

    def deletar_atual(self):
        if self.__primeiro.proximo is None:
            self.deletar_primeiro()
        elif self.__atual.proximo is None:
            self.deletar_ultimo()
        elif self.__atual == self.__primeiro:
            self.deletar_primeiro()
        else:
            self.__atual.anterior.proximo = self.__atual.proximo
            self.__atual.proximo.anterior = self.__atual.anterior
            self.__atual = self.__atual.anterior
 
    def deletar_elemento(self, chave):
        self.__mover_primeiro()
        while self.__atual.proximo != None and self.__atual.chave != chave:
            self.__atual = self.__atual.proximo

        if self.__atual.chave == chave:
            self.deletar_atual()

    def deletar_posicao(self, indice):

        self.__mover_primeiro()
        self.__avancar(indice)
        self.deletar_atual()



