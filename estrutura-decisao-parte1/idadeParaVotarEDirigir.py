from datetime import datetime

anoNascimento = int(input("Informe o ano de nascimento da pessoa com 4 dígitos (Ex. 1990): "))
now = datetime.now()
anoAtual = now.year

idade = anoAtual - anoNascimento

if idade >= 18:
    print("\nA pessoa já tem idade(", idade, ") para tirar carteira de habilitação e votar.")
    exit(0)

if idade >= 16:
    print("\nA pessoa tem idade(", idade, ") somenta para votar.")
    exit(0)

print("\nA pessoa não tem idade(", idade, ") nem para votar e nem para tirar carteira de habilitação.")