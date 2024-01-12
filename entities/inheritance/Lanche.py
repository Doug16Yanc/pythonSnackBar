class Lanch(Prato):
    def __init__(self, id, nome, quantidade, preco, pao, recheio, molho):
        super().__init__(id, nome, quantidade, preco)
        self.pao = pao
        self.recheio = recheio
        self.molho = molho

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

        @preco.setter
        def preco(self, molho):
            self._molho = molho
