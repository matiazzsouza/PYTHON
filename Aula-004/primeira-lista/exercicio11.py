def boletim(nota1, nota2, frequencia):

    media = (nota1 + nota2)/2

    if media >= 6:
        sit = "Aprovado"
    else:
        sit = "Reprovado"
    
    if frequencia >= 75:
        sitf = "Aprovado"
    else:
        sitf = "Reprovado"
    
    if sit == "Aprovado" and sitf == "Aprovado":
        sitfinal = "Aprovado"
    else:
        sitfinal = "Reprovado"

    return media, sit, sitf, sitfinal
    
def main():

    print("-"*60)
    print("\t\tBOLETIM ESCOLAR")
    print("-"*60)

    nome = input("\nDigite o nome do aluno: ")

    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))

    frequencia = float(input("Digite a frequência do aluno: "))

    media, sit, sitf, sitfinal = boletim(nota1, nota2, frequencia)

    print("\n")
    print("-"*60)
    print(f"RESULTADO DO ALUNO {nome.upper()}:")
    print(f"notas: {media} = {sit}")
    print(f"frequencia: {frequencia} = {sitf}")
    print(f"resultado final: {sitfinal}")
    print("-"*60)
    
main()