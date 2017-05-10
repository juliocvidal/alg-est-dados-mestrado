temperaturas = [0] * 12
meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

maior = 0
menor = 1000000
indiceMaior = 0
indiceMenor = 0

for i in range(12):
    temperaturas[i] = int(input("\nInforme a temperatura do mês de %s: " % meses[i]))
    
    if temperaturas[i] > maior:
        maior = temperaturas[i]
        indiceMaior = i

    if temperaturas[i] < menor:
        menor = temperaturas[i]
        indiceMenor = i

print("\nMeses: ", meses)
print("\nTemperaturas: ", temperaturas)
print("\nA maior temperatura foi ", temperaturas[indiceMaior], "º no mês de ", meses[indiceMaior])
print("\nA menor temperatura foi ", temperaturas[indiceMenor], "º no mês de ", meses[indiceMenor])



