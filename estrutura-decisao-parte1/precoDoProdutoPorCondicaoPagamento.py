precoProduto = float(input("Informe o preço do produto: "))

print("Informe a forma de pagamento (1-4) conforme a tabela abaixo: ")

print("1 - À vista em dinheiro ou cheque, recebe 20% de desconto")
print("2 - À vista no cartão de crédito, recebe 10% de desconto")
print("3 - Em duas vezes, preço normal da etiqueta sem juros")
print("4 - Em três vezes, preço normal de etiqueta mais juros de 5%")

formaPagamento = int(input(""))

desconto = 0

if formaPagamento == 1:
    desconto = 0.2

if formaPagamento == 2:
    desconto = 0.1

if formaPagamento == 4:
    desconto = -0.05

descontoAplicado = precoProduto * desconto
precoFinal = precoProduto - descontoAplicado

print("O preço final a ser pago será: ", precoFinal)