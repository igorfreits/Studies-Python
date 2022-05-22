"""
Como criar pacotes e módulos
"""
from dados import aumento, redução
import dadosone

preço = 49.90
# Valor formatado do modulo dadosone
preço_com_aumento = aumento(preço, 15, formata=True)
print(preço_com_aumento)

preço = 49.90
preço_com_redução = redução(preço, 15)
print(preço_com_redução)

print(dadosone.real(100))
