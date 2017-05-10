entrada = str(input("Informe os N elementos do vetor (Ex. 1,2,3,4): "))

a = entrada.split(',')
tamanhoDeA = len(a)

positivos = negativos = 0

for i in range(tamanhoDeA):
    if int(a[i]) >= 0:
        positivos += 1
    else:
        negativos += 1

print("\nA:", a)
print("\nPositivos: ", positivos, "\nNegativos: ", negativos)
