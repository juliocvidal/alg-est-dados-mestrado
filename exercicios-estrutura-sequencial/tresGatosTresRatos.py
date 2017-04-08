gatos = int(input("Informe a quantidade de gatos:\n"))
ratos = int(input("Informe a quantidade de ratos:\n"))

gatosIniciais = 3
ratosIniciais = 3
tempoInicial = 3

razaoGatoPorRatoInicial = gatosIniciais / ratosIniciais

#Tempo que sera usado para calcular independente da quantiade de gatos e ratos
tempoGastoGatoPorRato = tempoInicial / razaoGatoPorRatoInicial


#100 100 x
razaoGatoPorRato = gatos / ratos

tempoFinal = tempoGastoGatoPorRato /razaoGatoPorRato

print(gatos, " gatos levarao ", tempoFinal, " minutos para matar ", ratos, " ratos.\n")

