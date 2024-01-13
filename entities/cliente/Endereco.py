class Endereco:
    def __init__(self, rua, numero, bairro, municipio, cep):
        self._rua = rua
        self._numero = numero
        self._bairro = bairro
        self._municipio = municipio
        self._cep = cep

        @property
        def rua(self):
            return self._rua

        @rua.setter
        def rua(self, rua):
            self._rua = rua
            
        @property  
        def numero(self):
            return self._numero
        
        @numero.setter
        def numero(self, numero):
            self._numero = numero

        @property
        def bairro(self):
            return self._bairro

        @bairro.setter
        def quantidade(self, bairro):
            self._bairro = bairro

        @property
        def municipio(self):
            return self._municipio

        @municipio.setter
        def preco(self, municipio):
            self._municipio = municipio

        @property
        def cep(self):
            return self._cep

        @cep.setter
        def cep(self, cep):
            self._cep = cep