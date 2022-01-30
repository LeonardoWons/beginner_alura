from abc import abstractmethod
import abc
from typing import List

from constantes import VALOR_PADRAO_MAXIMO, VALOR_PADRAO_MINIMO 


class FilaBase(metaclass=abc.ABCMeta):
    
    def __init__(self) -> None:
        
        self.codigo: int = VALOR_PADRAO_MINIMO 
        self.fila: List[str] = []
        self.clientes_atendidos: List[str] = []
        self.senha_atual: str = ""

    def reseta_fila(self) -> None:
        if self.codigo >= VALOR_PADRAO_MAXIMO:
            self.codigo = VALOR_PADRAO_MINIMO
        else:
            self.codigo += 1

    def inserir_cliente(self):
        self.fila.append(self.senha_atual)

    def atualiza_fila(self):
        self.reseta_fila()
        self.gera_senha_atual()
        self.inserir_cliente()

    @abstractmethod
    def gera_senha_atual(self):
        ...

    @abstractmethod
    def chama_cliente(self, caixa: int):
        ...
    