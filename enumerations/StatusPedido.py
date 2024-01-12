from enum import Enum

class StatusPedido(Enum):
    NÃO_FEITO = 1,
    PENDENTE = 2,
    EM_PROGRESSO = 3,
    ENTREGUE = 4