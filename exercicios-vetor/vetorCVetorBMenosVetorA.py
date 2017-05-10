entrada = str(input("Informe os N elementos do vetor A(Ex. 1,2,3,4): "))
a = entrada.split(',')
entrada = str(input("Informe os N elementos do vetor B(Ex. 1,2,3,4): "))
b = entrada.split(',')

tamanho = len(a)
c = [0] * tamanho

for i in range(tamanho):
    c[i] = int(b[i]) - int(a[i])

print(c)
