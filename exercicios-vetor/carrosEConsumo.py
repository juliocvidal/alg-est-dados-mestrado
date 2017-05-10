carros = str(input("Digite os nomes dos carros (Ex: Palio, Gol, Uno, Celta, Corsa)\n"))
consumo = str(input("Digite os consumos dos carros (Ex: 10.0, 5, 3, 4, 2)\n"))

carros = carros.split(",")
consumos = consumo.split(",")

melhorConsumo = 0
indiceMelhorCosumo = 0

for i in range(len(consumos)):
    if float(consumos[i]) > melhorConsumo:
        melhorConsumo = float(consumos[i])
        indiceMelhorCosumo = i

carroMelhorConsumo = carros[indiceMelhorCosumo]

print("\nO carro mais econômico é o", carroMelhorConsumo, ".")
print("\nEle consome", 1000 / melhorConsumo, "litros para percorrer 1000 km.")