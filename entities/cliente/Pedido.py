class Pedido:
    def __init__(self, cliente, statusPedido, formaPagamento, taxaServico, itensConsumidos):
        self.cliente = cliente
        self.statusPedido = statusPedido
        self.taxaServico = taxaServico
        self.formaPagamento = formaPagamento

        if not isinstance(itensConsumidos, list):
            raise TypeError("itensConsumidos deve ser uma lista")
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
    def formaPagamento(self):
        return self._formaPagamento

    @formaPagamento.setter
    def formaPagamento(self, formaPagamento):
        self._formaPagamento = formaPagamento

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
