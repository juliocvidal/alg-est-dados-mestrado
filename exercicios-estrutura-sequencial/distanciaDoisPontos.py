import math

x1 = int(input("informe coordenada X do ponto P: "))
y1 = int(input("informe coordenada Y do ponto P: "))
x2 = int(input("informe coordenada X do ponto Q: "))
y2 = int(input("informe coordenada Y do ponto Q: "))

distancia = math.sqrt(pow((x2 - x1), 2) + pow((y2 - y1), 2))

print("A distancia entre os ponto P(", x1, ",", y1, ") e Q(", x2, ",", y2, ") é: ", distancia)