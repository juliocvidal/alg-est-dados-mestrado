# notas = [0, 0, 0]
#
# soma = 0
# i = 0
#
# while i < 3:
#     notas[i] = float(input("Nota %d: " % (i+1)))
#     soma += notas[i]
#     i += 1
#
#
# print("Media: %5.2f" % (soma/3))
import random

L = list(range(11))
random.shuffle(L)
print(L)
L.sort(reverse=False)
print(L)
