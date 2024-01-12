class Pizza(Prato):
    def __init__(self, id, nome, quantidade, preco, molho, recheio, borda):
        super().__init__(id, nome, quantidade, preco, molho, recheio, borda)
        self.molho = molho
        self.recheio = recheio
        self.borda = borda

        @property
        def molho(self):
            return self._molho

        @molho.setter
        def molho(self, molho):
            self._molho = molho

        @property
        def recheio(self):
            return self._recheio

        @recheio.setter
        def recheio(self, recheio):
            self._recheio = recheio

        @property
        def borda(self):
            return self._borda

        @borda.setter
        def borda(self, borda):
            self._borda = borda