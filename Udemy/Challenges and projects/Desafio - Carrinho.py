carrinho = []
carrinho.append(('Produto1', 30))
carrinho.append(('Produto2', 20))
carrinho.append(('Produto3', 50))

total = sum([float(y) for x, y in carrinho])
print(carrinho)
print(total)
