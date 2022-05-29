"""Associação(POO)"""
from classes import Writer, Pen, TypeWriter
# Relação de associação
"""Se relaciona com outra classe ou seja vai estar associada a outra classe.
Mas nenhuma das duas classes dependem uma da outra.
Ambas as classes podem viver uma sem a outra."""


escritor = Writer('Alice')
caneta = Pen('Bic')
maquina = TypeWriter


print(escritor.name)
print(caneta.brand)
maquina.write(maquina)

escritor.tool = maquina
escritor.tool.write(maquina)
# Tool esta recebendo o objeto da classe inteira

del escritor

print(caneta.brand)
maquina.write(maquina)
