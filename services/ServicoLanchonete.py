from entities.pratos.Pizza import Pizza
from entities.pratos.Lanche import Lanche
from entities.pratos.Salgadinho import Salgadinho



class ServicoLanchonete:

    def __init__(self):
        self.itensDisponiveis = []

    def armazenarDados(self):
        pizza1 = Pizza(id = 1, nome = "Bolonhesa", quantidade = 120, preco = 25.00, molho = "", recheio = "catupiry", borda = "peperoni")

        self.itensDisponiveis.append(pizza1)

    def mostrarDisponiveis(self):
        for prato in self.itensDisponiveis:
            print(f"Id : {prato.id}\t nome : {prato.nome}\t preco : {prato.preco}\n")
