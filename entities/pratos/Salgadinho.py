class Salgadinho(Prato):
    def __init__(self, id, nome, quantidade, preco, recheio, massa):
        super().__init__(id, nome, quantidade, preco)
        self._recheio = recheio
        self._massa = massa

        @property
        def recheio(self):
            return self._recheio

        @recheio.setter
        def recheio(self, recheio):
            self._recheio = recheio

        @property
        def massa(self):
            return self._massa

        @massa.setter
        def massa(self, massa):
            self._massa = massa

    