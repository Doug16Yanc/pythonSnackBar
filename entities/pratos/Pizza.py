from entities.pratos.Prato import Prato

class Pizza(Prato):
    def __init__(self, id, tipo, nome, quantidade, preco, molho, recheio, borda):
        super().__init__(id, tipo, nome, quantidade, preco)
        self._molho = molho
        self._recheio = recheio
        self._borda = borda

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