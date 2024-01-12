class Pedido:
    def __init__(self, cliente, statusPedido taxaServico, itensConsumidos):
        self.cliente = cliente
        self.statusPedido = statusPedido
        self.taxaServico = taxaServico

        if not isinstance(list, itensConsumidos):
            raise TypeError("Error")
        self.itensConsumidos = itensConsumidos

        @property
        def cliente(self):
            return self._cliente

        @cliente.setter
        def cliente(self, cliente):
            self._cliente = cliente

        @property
        def statusPedido(self):
            return self._statusPedido

        @statusPedido.setter
        def statusPedido(self, statusPedido):
            self._statusPedido = statusPedido

        @property
        def taxaServico(self):
            return self._taxaServico

        @taxaServico.setter
        def taxaServico(self, taxaServico):
            self._taxaServico = taxaServico

        @property
        def itensConsumidos(self):
            return self._itensConsumidos

        @itensConsumidos.setter
        def itensConsumidos(self, itensConsumidos):
            if not isinstance(itensConsumidos, list):
                raise TypeError("itensConsumidos deve ser uma lista")
            self._itensConsumidos = itensConsumidos