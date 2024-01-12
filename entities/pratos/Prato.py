class Prato:
    def __init__(self, id, nome, quantidade, preco):
        self._id = id
        self._nome = nome
        self._quantidade = quantidade
        self._preco = preco



        @property
        def id(self):
            return self._id

        @id.setter
        def id(self, id):
            self._id = id
            
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