class Lanche:
    def __init__(self, id, nome, quantidade, preco):
        self.id = id
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco

       

        @property
        def id(self):
            return self._codigo

        @id.setter
        def id(self, codigo):
            self._codigo = codigo
            
        @property  
        def nome(self):
            return self._nome
        
        @nome.setter
        def nome(self, nome):
            self._nome = nome

        @property
        def quantidade(self):
            return self._quantidade

        @quantidade.setter
        def quantidade(self, quantidade):
            self._quantidade = quantidade

        @property
        def preco(self):
            return self._preco

        @preco.setter
        def preco(self, preco):
            self._preco = preco