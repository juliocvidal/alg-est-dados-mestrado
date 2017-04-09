from math import ceil

custoFesta = float(input("Informe o custo da festa de formatura: "))
precoConvite = float(input("Informe o preço do convite: "))

#Arredondando para o proximo numero inteiro já que não é possível vender convites fracionarios. =)
convitesNecessarios = ceil(custoFesta / precoConvite)

print("Devem ser vendidos pelo menos ", convitesNecessarios, "convites.")