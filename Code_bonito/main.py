#from fila_normal import FilaNormal
#from fila_prioritaria import FilaPrioritaria
from factory import FactoryFila
from estatistica_detail import EstatisticaDetail
from estatistica_simples import EstatisticaSimples


#fila_teste = FilaNormal()
#fila_teste.atualiza_fila()
#fila_teste.atualiza_fila()
#print(fila_teste.chama_cliente(10))
#print(fila_teste.chama_cliente(3))

factory_teste = FactoryFila.pega_fila("prioritaria")
factory_teste.atualiza_fila()
factory_teste.atualiza_fila()
factory_teste.atualiza_fila()
print(factory_teste.chama_cliente(10))
print(factory_teste.chama_cliente(3))
print(factory_teste.estatistica("10/10/10", 100, EstatisticaSimples))