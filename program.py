from utilidades.Util import Util
from services.ServicoLanchonete import ServicoLanchonete

def interagePrimeiro():
    Util.imprimeMensagem("Bem-vindo(a) à lanchonete Tocatta and Fügue\n")
    servicoLanchonete = ServicoLanchonete()
    servicoLanchonete.armazenarDados()
    servicoLanchonete.mostrarDisponiveis()

def main():
    interagePrimeiro()

if __name__ == "__main__":
    main()