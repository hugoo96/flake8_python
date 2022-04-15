from fabrica_fila import FabricaFila

fila = FabricaFila.pega_fila('prioritaria')

fila.atualiza_fila()
fila.atualiza_fila()

print(fila.chama_cliente(10))
print(fila.chama_cliente(5))

print(fila.estatistica('15/04/2022', 1898, 'detail'))
