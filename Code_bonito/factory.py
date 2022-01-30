from constantes import TIPO_FILA_NORMAL, TIPO_FILA_NORMAL_NM, TIPO_FILA_PRIORITARIA, TIPO_FILA_PRIORITARIA_PR, TIPO_FILA_DISPONIVEL
from fila_normal import FilaNormal
from fila_prioritaria import FilaPrioritaria

from typing import Union


class FactoryFila:

    @staticmethod
    def pega_fila(tipo) -> Union[FilaNormal, FilaPrioritaria]:
        if tipo == TIPO_FILA_NORMAL:
            return FilaNormal()

        elif tipo == TIPO_FILA_NORMAL_NM:
            return FilaNormal()

        elif tipo == TIPO_FILA_PRIORITARIA:
            return FilaPrioritaria()
        
        elif tipo == TIPO_FILA_PRIORITARIA_PR:
            return FilaPrioritaria()
        
        else:
            raise NotImplementedError(f"tipos de fila disponiveis: {TIPO_FILA_DISPONIVEL}")