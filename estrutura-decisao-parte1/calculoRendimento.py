deposito = float(input("Informe o valor do depósito: "))
taxaJuros = float(input("Informe o valor da taxa de juros de 0 a 100 (Ex 1.5 para 1.5%):"))

rendimento = deposito * taxaJuros/100

valorDepoisDoRendimento = deposito + rendimento

print("\nO rendimento sobre o deposito de ", deposito, "aplicando a taxa de juros de", taxaJuros, "% foi de", rendimento)
print("O valor obtido após o rendimento é:", valorDepoisDoRendimento)
