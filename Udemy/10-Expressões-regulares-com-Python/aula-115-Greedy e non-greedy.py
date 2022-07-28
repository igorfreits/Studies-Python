"""Greedy e non-greedy (lazy)"""

import re
# Frase Ambígua
# Greedy - Guloso(Pega a frase inteira)
# Non-greedy - Mínimo de informação(Pega o que está disponível)
texto = ''''
<p>Frase</p> <p>phrase</p> <p>段階</p> <div>фраза</div> <div></div>
'''
print(re.findall(r'<[pdiv]{1,3}>.*?<\/[pdiv]{1,3}>', texto))  # non-greedy
print(re.findall(r'<[pdiv]{1,3}>.+?<\/[pdiv]{1,3}>', texto))  # non-greedy

print(re.findall(r'<[pdiv]{1,3}>.*', texto))
