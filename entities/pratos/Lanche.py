from entities.pratos.Prato import Prato

class Lanche(Prato):
    def __init__(self, id, tipo, nome, quantidade, preco, pao, recheio, molho):
        super().__init__(id, tipo, nome, quantidade, preco)
        self._pao = pao
        self._recheio = recheio
        self._molho = molho

        @property
        def pao(self):
            return self._pao

        @pao.setter
        def pao(self, pao):
            self._pao = pao

        @property
        def recheio(self):
            return self._recheio

        @recheio.setter
        def recheio(self, recheio):
            self._recheio = recheio

        @property
        def molho(self):
            return self._molho

        @molho.setter
        def molho(self, molho):
            self._molho = molho
