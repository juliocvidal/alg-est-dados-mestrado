tempoGasto = float(input("Informe o tempo gasto na viagem (h): "))
velocidadeMedia = float(input("Informe a velocidade media (km/h): "))

distanciaPercorrida = tempoGasto * velocidadeMedia #km

#12km por litro
litrosUsados = distanciaPercorrida / 12

print("Velocidade média: ", velocidadeMedia, "km/h")
print("Tempo gasto: ", tempoGasto, "hora(s)")
print("Distância percorrida: ", distanciaPercorrida, "km")
print("Quantidade de litros utilizados na viagem: ", litrosUsados, "litro(s)")