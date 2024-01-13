from enum import Enum

class FormaPagamento(Enum):
    DINHEIRO = "Dinheiro"
    CARTÃO = "Cartão"
    PIX = "Pix"

    def __str__(self):
        return self.value
