aluno = input("Digite o nome do aluno:\n")
disciplina = input("Informe a disciplina:\n")
nota1 = float(input("Informe a primeira nota:\n"))
nota2 = float(input("Informe a segunda nota:\n"))
nota3 = float(input("Informe a terceira nota:\n"))
nota4 = float(input("Informe a quarta nota:\n"))

media = (nota1 + nota2 + nota3 + nota4) / 4

if media < 5:
    print("Aluno ", aluno, " reprovado na disciplina ", disciplina, " com media ", media, "\n")
else:
    if media < 7:
        print("Aluno ", aluno, " ficou de final na disciplina ", disciplina, " com media ", media, "\n")
    else:
        print("Aluno ", aluno, " aprovado na disciplina ", disciplina, " com media ", media, "\n")