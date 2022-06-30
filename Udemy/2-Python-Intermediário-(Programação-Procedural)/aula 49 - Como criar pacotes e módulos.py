"""
Como criar pacotes e módulos
"""
from one_data import aumento, redução
import one_data

preço = 49.90
# Valor formatado do modulo one_data
preço_com_aumento = aumento(preço, 15, formata=True)
print(preço_com_aumento)

preço = 49.90
preço_com_redução = redução(preço, 15)
print(preço_com_redução)

print(one_data.real(100))
