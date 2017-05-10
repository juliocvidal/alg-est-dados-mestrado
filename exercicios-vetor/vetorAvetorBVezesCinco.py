tam = int(input('Digite o tamanho do vetor: '))
A=[0]*tam
B=[0]*tam
i=0
for i in range (tam):
    A[i]=int(input("Digite o elemento %d do vetor: " %i ))
    B[i]=A[i]*5
i=0

while i<tam:
    print("\nVetor A : %d\t vetor B: %d " %(A[i] , B[i]))
    i=i+1