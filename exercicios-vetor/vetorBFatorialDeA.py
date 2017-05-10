entrada = str(input("Informe os N elementos do vetor (Ex. 1,2,3,4): "))

a = entrada.split(',')
tamanhoDeA = len(a)

b = [0] * tamanhoDeA

for i in range(tamanhoDeA):
    fatorial = int(a[i])
    sum = 1
    while fatorial > 0:
        sum *= fatorial
        fatorial -= 1
    b[i] = sum

print("\nB: ", b)


