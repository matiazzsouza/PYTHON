def main():

    alunos = []

    qnt = int(input("\nDigite quantos alunos voce deseja inserir:"))
    media = 0
    resultado = ""


    for i in range(qnt):
        resultado = ""
        nome = input(f"\nDigite o nome do {i + 1}° aluno:")
        ra = i #fiz o RA sendo como um ID
        print("\n")
        
        nota1 = int(input("Digite a primeira nota do aluno(a):"))
        nota2 = int(input("Digite a segunda nota do aluno(a):"))
        nota3 = int(input("Digite a terceira nota do aluno(a):"))
        nota4 = int(input("Digite a ultima nota do aluno(a):"))

        media = (nota1 + nota3 + nota2 + nota4) / 4
        
        if(media >= 5):
            resultado += "Aprovado"
        else:
            resultado += "Reprovado"


        cadastro = [nome,ra,nota1,nota2, nota3, nota4, media, resultado]
        alunos.append(cadastro)

    
    print("-" * 90)

    print(f"|{'Nome':<15} | {'RA':<10} | {'Nota 1':^7} | {'Nota 2':^7} | {'Nota 3':^7} | {'Nota 4':^7} | {'Média':^7} | {'Resultado':^8}|")    

    print("-" * 90)

    
    for i in range(qnt):
        for j in range(8):

            if (j == 0):       
                print(f"|{alunos[i][j]:<15}", end=" | ")

            elif (j == 1):     
                print(f"{alunos[i][j]:<10}", end=" | ")

            elif (2 <= j <= 5 ):  
                print(f"{alunos[i][j]:^7}", end=" | ")

            elif (j == 6):    
                print(f"{alunos[i][j]:^7.2f}", end=" | ")

            elif (j == 7):     
                print(f"{alunos[i][j]:<7}", end=" | ")
                
        print()
        print("-" * 90)
        
        

main()