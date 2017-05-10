entrada = str(input("Informe os N elementos do vetor (Ex. 1,2,3,4): "))

a = entrada.split(',')
tamanhoDeA = len(a)

primos = 0
vetorDePrimos = [0] * tamanhoDeA

for i in range(tamanhoDeA):
    atual = int(a[i])
    dividendo = atual - 1
    divisoesExatas = 0

    while dividendo > 1:
        resto = atual % dividendo
        if resto == 0:
            divisoesExatas += 1
        dividendo -= 1

    if divisoesExatas == 0:
        vetorDePrimos[primos] = atual
        primos += 1


print("\nA: ", a)
print("\nQuantidade de primos: ", primos)
print("\nPrimos: ", vetorDePrimos)
