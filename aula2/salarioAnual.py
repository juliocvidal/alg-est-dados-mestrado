funcionario = input("Informe o nome do funcionario:\n")
salario = float(input("Informe o salario anual:\n"))

if salario > 25000:
    print("Funcionario ", funcionario, " deve pagar 20% de imposto.\n")
    exit(0)

if 25000 >= salario > 20000:
    print("Funcionario ", funcionario, " deve pagar 15% de imposto.\n")
    exit(0)

if 20000 >= salario > 15000:
    print("Funcionario ", funcionario, " deve pagar 10% de imposto.\n")
    exit(0)

if 15000 >= salario > 10000:
    print("Funcionario ", funcionario, ' deve pagar 5% de imposto.\n')
    exit(0)

print("Funcionario ", funcionario, " isento de impostos\n")




