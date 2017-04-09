votos = list(map(int, input("Informe a sequencia de votos (Ex: 1 1 1 2 3 6 6 5 4 1): ").split()))

votosComputados = [0] * 6

for voto in votos:
    votosComputados[voto - 1] += 1

totalDeVotos = len(votos)

print("\nTotal de votos: ", totalDeVotos)
print("Votos computados: ", votosComputados, "\n")

for i in range(4):
    print("O candidato ", i + 1, " teve", votosComputados[i], "votos. O que representa ", votosComputados[i]*100/totalDeVotos,
          "% do total.")

print("Houveram", votosComputados[4], "votos nulos. O que representa ", votosComputados[4]*100/totalDeVotos,
          "% do total.")

print("E", votosComputados[5], "votos em branco. O que representa ", votosComputados[5]*100/totalDeVotos,
          "% do total.")




