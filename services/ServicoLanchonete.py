from entities.pratos.Prato import Prato
from entities.pratos.Pizza import Pizza
from entities.pratos.Lanche import Lanche
from entities.pratos.Salgadinho import Salgadinho


<<<<<<< HEAD
=======
class ServicoLanchonete:

    def __init__(self):
        self.itensDisponiveis = []

    def armazenarDados(self):
        pizza1 = Pizza( nome="Bolonhesa", quantidade=120, preco=25.00, molho="", recheio="catupiry", borda="peperoni")

        self.itensDisponiveis.append(pizza1)

    def mostrarDisponiveis(self):
        for prato in self.itensDisponiveis:
            print(f"Id : {prato.id}\t nome : {prato.nome}\t preco : {prato.preco}\n")
>>>>>>> 33a60449ccb0460c93de369dc81a5eb1be5c93d6
