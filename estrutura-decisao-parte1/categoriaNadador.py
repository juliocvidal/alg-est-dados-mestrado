idadeNadador = int(input("Informe a idade do nadador: "))

if idadeNadador < 5:
    print("Categoria Infantil.")

if 5 <= idadeNadador < 10:
    print("Categoria Juvenil.")

if 10 <= idadeNadador < 16:
    print("Categoria Adolescente.")

if 16 <= idadeNadador < 25:
    print("Categoria Adulto.")

if idadeNadador >= 25:
    print("Categoria Senior.")