tam = int(input('Digite o tamanho do vetor: '))
A=[0]*tam
i=0

for i in range (tam):
    A[i]=int(input("digite o elemento %d do vetor: " %i))

i=0
while i<tam:
    print("\nvetor A : %d " % A[i])
    i=i+1