import uuid

from entities.cliente.Cliente import Cliente
from entities.cliente.Endereco import Endereco
from entities.pratos.Pizza import Pizza
from utilidades.Util import Util


class ServicoCliente:

    def __init__(self):
        self.itensDisponiveis = []
        pizza1 = Pizza(id=1, nome="Portuguesa", quantidade=120, preco=25.00, molho="tomate", recheio="pepperoni", borda="catupiry")
        pizza2 = Pizza(id=2, nome="Muçarela", quantidade=120, preco=25.00, molho="alfredo", recheio="requeijão", borda="cheddar")
        pizza3 = Pizza(id=3, nome="Marguerita", quantidade=120, preco=25.00, molho="bechamel", recheio="frango", borda="pão")

        self.itensDisponiveis.append(pizza1)
        self.itensDisponiveis.append(pizza2)
        self.itensDisponiveis.append(pizza3)


    def fazerPedido(self):
        self.itensConsumidos = []
        Util.imprimeMensagem("Itens disponíveis:\n")

        while True:
            for i, prato in enumerate(self.itensDisponiveis):
                print(f"{prato._id}\t{prato._nome}\t{prato._quantidade}\t\t{prato._preco}\t{prato._recheio}, {prato._molho}, {prato._borda}")

            validacao = input("Digite o código do item ou -1 se quiser encerrar:")

            if validacao != "-1":
                try:
                    codigo_item = int(validacao)
                    prato_encontrado = next((prato for prato in self.itensDisponiveis if prato._id == codigo_item), None)

                    if prato_encontrado:
                        quantidade = int(input(f"Digite a quantidade de {prato_encontrado._nome} que desejas:"))

                        if quantidade <= prato_encontrado._quantidade and quantidade > 0:
                            print(f"Aquisição de {quantidade} {prato_encontrado._nome}(s) realizada(s) com sucesso!\n")
                            prato_encontrado._quantidade -= quantidade
                            self.itensConsumidos.append((prato_encontrado, quantidade))
                        else:
                            print("Quantidade não possível.\n")
                    else:
                        print("Item não encontrado.\n")
                except ValueError:
                    print("Digite um código válido.\n")
            else:
                break

        self.processaDadosCliente()

    def processaDadosCliente(self):
        id = str(uuid.uuid4())
        nome = input("Nome do cliente:")
        cpf = input("CPF do cliente:")
        rua = input("Rua:")
        numero = int(input("Número do domícilio:"))
        bairro = input("Bairro:")

        cliente = Cliente(id, nome, cpf, Endereco(rua, numero, bairro, municipio="Pedra Branca", cep=63630000))

        self.realizaPagamento(cliente)


    def realizaPagamento(self, cliente):
        gasto = self.calculaTaxaServico()
        Util.imprimeMensagem(f"Gasto total: R$ {gasto}.\n")

        self.geraComprovante(cliente)

    def calculaTaxaServico(self):
        valorFinal = 0.0
        for prato, quantidade in self.itensConsumidos:
            valorFinal += prato._preco * quantidade
        return valorFinal

    def geraComprovante(self, cliente):
        Util.imprimeMensagem("Dados do cliente:\n")
        print(f"> Nome do cliente: {cliente._nome}"
              f"> Id do indivíduo: {cliente.id}\n"
              f"> bairro do cliente: {cliente._endereco._bairro}\n")
        Util.imprimeMensagem("Dados de compra:\n")
        for i, prato in enumerate(self.itensConsumidos):
            print(f"{prato._id}\t{prato._nome}\t{prato._quantidade}\t\t{prato._preco}\n")






