from fabrica_fila import FabricaFila
from estatistica_resumida import EstatisticaResumida
from estatistica_detalhada import EstatisticaDetalhada

fila = FabricaFila.pega_fila('prioritaria')

fila.atualiza_fila()
fila.atualiza_fila()

print(fila.chama_cliente(10))
print(fila.chama_cliente(5))

print(fila.estatistica(EstatisticaDetalhada("17/04/2022", 1898)))
print(type(fila.estatistica))
