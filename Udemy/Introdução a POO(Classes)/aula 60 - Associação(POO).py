"""Associação(POO)"""
from whiterclass import Writer
from whiterclass import Pen
from whiterclass import TypeWriter
# Relação de associação
"""Se relaciona com outra classe ou seja vai estar associada a outra classe.
Mas nenhuma das duas classes dependem uma da outra.
Ambas as classes podem viver uma sem a outra."""

"""Na associação uma classe "usa" código de outra classe,
mas não depende inteiramente disso para funcionar"""


escritor = Writer('Isra')
caneta = Pen('Bic')
maquina = TypeWriter


print(escritor.name)
print(caneta.brand)
maquina.write(maquina)

escritor.tool = maquina
escritor.tool.write(maquina)
# Tool esta recebendo o objeto da classe inteira
# Associação entre o escritor e uma caneta/maquina de escrever

del escritor

# Caneta e maquina funcionam mesmo depois de apagar a classe escritor
print(caneta.brand)
maquina.write(maquina)
