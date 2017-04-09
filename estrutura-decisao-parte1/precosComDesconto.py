codigo = int(input("Informe o codigo do produto: "))
precoAtual = float(input("Informe o preço atual do produto: "))
desconto = 0
novoPreco = precoAtual

if precoAtual > 500:
    desconto = 0.2

if 100 < precoAtual <= 500:
    desconto = 0.1


descontoAplicado = precoAtual * desconto
novoPreco = precoAtual - descontoAplicado

print("\nO desconto a ser aplicado será de", desconto * 100, "%. Que representa um descont real de", descontoAplicado)
print("O novo preco do produto de codigo", codigo, "será", novoPreco)
