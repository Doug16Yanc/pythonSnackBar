import uuid

from entities.cliente.Cliente import Cliente
from entities.cliente.Endereco import Endereco
from entities.cliente.Pedido import Pedido
from entities.pratos.Lanche import Lanche
from entities.pratos.Pizza import Pizza
from entities.pratos.Salgadinho import Salgadinho
from enumerations.FormaPagamento import FormaPagamento
from enumerations.StatusPedido import StatusPedido
from utilidades.Util import Util


class ServicoCliente:

    def __init__(self):
        self.itensDisponiveis = []
        pizza1 = Pizza(id=1, tipo = "Pizza", nome="Portuguesa", quantidade=120, preco=28.00, molho="tomate", recheio="pepperoni", borda="catupiry")
        pizza2 = Pizza(id=2, tipo = "Pizza", nome="Muçarela", quantidade=120, preco=25.00, molho="alfredo", recheio="requeijão", borda="cheddar")
        pizza3 = Pizza(id=3, tipo = "Pizza", nome="Marguerita", quantidade=120, preco=29.00, molho="bechamel", recheio="frango", borda="pão")

        lanche1 = Lanche(id = 4, tipo="Lanche", nome= "esfirra", quantidade=150, preco=3.50,  pao="branco", recheio="calabresa", molho="catshup mostarda")
        lanche2 = Lanche(id = 5, tipo="Lanche", nome= "cachorro quente", quantidade=180, preco=4.00,  pao="brioche", recheio="salsiha", molho="catupiry")
        lanche3 = Lanche(id = 6, tipo="Lanche", nome= "hambúrguer", quantidade=135, preco=5.00,  pao="italiano", recheio="carne moída", molho="requeijão")

        salgado1 = Salgadinho(id = 7, tipo="Salgadinho", nome= "coxinha", quantidade=200, preco=2.00, recheio="carne de frango", massa="trigo")
        salgado2 = Salgadinho(id = 8, tipo="Salgadinho", nome= "pastel", quantidade=100, preco=5.00, recheio="carne de sol", massa="trigo")
        salgado3 = Salgadinho(id = 9, tipo="Salgadinho", nome= "risole", quantidade=160, preco=2.50, recheio="presunto/muçarela", massa="trigo")


        self.itensDisponiveis.append(pizza1)
        self.itensDisponiveis.append(pizza2)
        self.itensDisponiveis.append(pizza3)

        self.itensDisponiveis.append(lanche1)
        self.itensDisponiveis.append(lanche2)
        self.itensDisponiveis.append(lanche3)

        self.itensDisponiveis.append(salgado1)
        self.itensDisponiveis.append(salgado2)
        self.itensDisponiveis.append(salgado3)

    def fazerPedido(self):
        self.itensConsumidos = []
        Util.imprimeMensagem("Itens disponíveis:\n")

        while True:
            Util.imprimeMensagem("Id\t nome\t quantidade\t preço\t informações do prato\n")
            for i, prato in enumerate(self.itensDisponiveis):
                if (prato._tipo == "Pizza"):
                    Util.imprimeMensagem("Pizzas:")
                    print(f"{prato._id}\t{prato._nome}\t{prato._quantidade}\t\t{prato._preco}\t{prato._recheio}, {prato._molho}, {prato._borda}")
                elif(prato._tipo == "Lanche"):
                    Util.imprimeMensagem("Lanches:")
                    print(f"{prato._id}\t{prato._nome}\t{prato._quantidade}\t\t{prato._preco}\t{prato._pao}, {prato._recheio}, {prato._molho}")
                elif(prato._tipo == "Salgadinho"):
                    Util.imprimeMensagem("Salgadinhos:")
                    print(f"{prato._id}\t{prato._nome}\t{prato._quantidade}\t\t{prato._preco}\t{prato._recheio}, {prato._massa}")

            validacao = input("\nDigite o código do item ou -1 se quiser encerrar:")

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
        pedido = Pedido(cliente._nome, gasto, StatusPedido.FEITO, FormaPagamento.DINHEIRO, self.itensConsumidos)
        Util.imprimeMensagem(f"Gasto total: R$ {round(gasto, 2)}.\n")
        opcaoPagamento = int(input("Forma de pagamento:\n"
                                   "(1) - Dinheiro\n"
                                   "(2) - Cartão\n"
                                   "(3) - Pix\n"))
        if opcaoPagamento == 1:
            DINHEIRO = FormaPagamento.DINHEIRO
            pedido._formaPagamento = DINHEIRO
            valor = float(input("Digite, em reais, o valor :"))

            if valor == gasto:
                print("Obrigado por sua preferência. Volte sempre!\n")
            elif valor > gasto:

                print(f"Valor do troco: R$ {round(self.calculaTroco(valor, gasto), 2)}\n")
            else:
                print("Valor não suficiente para realizar pagamento.\n")
                return
        elif opcaoPagamento == 2:
            CARTÃO = FormaPagamento.CARTÃO
            pedido._formaPagamento = CARTÃO
            print("Obrigado por sua preferência. Volte sempre!\n")
        elif opcaoPagamento == 3:
            PIX = FormaPagamento.PIX
            pedido._formaPagamento = PIX
            print("Obrigado por sua preferência. Volte sempre!\n")
        else:
            print("Opção não possível.\n")

        self.geraComprovante(cliente, gasto, pedido)

    def calculaTaxaServico(self):
        valorFinal = 0.0
        for prato, quantidade in self.itensConsumidos:
            valorFinal += prato._preco * quantidade
        return valorFinal*1.05 #Taxa de entrega

    def calculaTroco(self, valor, gasto):
        valorTroco = valor - gasto
        return valorTroco
    def geraComprovante(self, cliente, gasto, pedido):
        Util.imprimeMensagem("Dados do cliente:\n")
        print(f"> Nome do cliente: {cliente._nome}\n"
              f"> Id do indivíduo: {cliente._id}\n"
              f"> bairro do cliente: {cliente._endereco._bairro}\n")
        Util.imprimeMensagem("Dados de compra:\n")
        print("Id\t nome\t quantidade\t preço unitário\t preço total\n")
        for i, (prato, quantidade) in enumerate(self.itensConsumidos):
            print(f"{prato._id}\t{prato._nome}\t{quantidade}\t\t{prato._preco}\t\t{prato._preco*quantidade}\n")
        Util.imprimeMensagem(f"Dados de finanças:\n")
        print(f"> Valor total : R$ {round(gasto, 2)}\n"
              f"> Forma de pagamento : {pedido._formaPagamento}\n"
              )






