#Considere que o aumento dos funcionários de uma empresa é de 10% do salário atual
#mais um percentual de produtividade discutido com a empresa. Escrever um algoritmo que
#leia o número do funcionário, seu salário atual, e o índice de produtividade discutido com a
#empresa. Então, escreve o número do funcionário, seu aumento e o valor de seu novo
#salário.

funcionario = int(input("Informe o numero do funcionario: "))
salarioAtualFuncionario = float(input("Informe o salario atual do funcionario: "))
indiceProdutividade = float(input("Informe o indice de produtividade (de 0 a 100. Ex: 20 para 20%): "))

aumento = (salarioAtualFuncionario * 0.1) + (salarioAtualFuncionario * indiceProdutividade/100)
novoSalario = salarioAtualFuncionario + aumento

print("Funcionario: ", funcionario)
print("Aumento: ", aumento)
print("Novo Salario: ", novoSalario)