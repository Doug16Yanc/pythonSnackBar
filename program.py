from utilidades.Util import Util
from services.ServicoCliente import ServicoCliente

def interagePrimeiro():
    Util.imprimeMensagem("Bem-vindo(a) à lanchonete Tocatta and Fügue\n")

    servicoCliente = ServicoCliente()
    servicoCliente.fazerPedido()


def main():
    interagePrimeiro()

if __name__ == "__main__":
    main()