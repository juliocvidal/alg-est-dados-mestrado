entrada = str(input("Informe os N elementos do vetor (Ex. 1,2,3,4): "))
a = entrada.split(',')
entrada = str(input("Informe os N elementos do vetor B(Ex. 1,2,3,4): "))
b = entrada.split(',')

tamanhoDeA = len(a)
soma = 0

for i in range(tamanhoDeA):
    soma += int(a[i]) * int(b[i])

print("\nA: ", a)
print("\nB: ", b)
print("\nProduto Escalar: ", soma)
