entrada = str(input("Informe os N elementos do vetor (Ex. 1,2,3,4): "))

a = entrada.split(',')
tamanhoDeA = len(a)

b = [0] * tamanhoDeA

for i in range(tamanhoDeA):
    b[i] = pow(int(a[i]), 2)

print("\nB: ", b)