class Cliente:
    def __init__(self, id, nome, cpf, endereco):
        self._id = id
        self._nome = nome
        self._cpf = cpf
        self._endereco = endereco

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
        def numero(self, nome):
            self._nome = nome

        @property
        def cpf(self):
            return self._cpf

        @cpf.setter
        def quantidade(self, cpf):
            self._cpf = cpf

        @property
        def endereco(self):
            return self._endereco
        
        @endereco.setter
        def endereco(self, endereco):
            self._endereco = endereco
