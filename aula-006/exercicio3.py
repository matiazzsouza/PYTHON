def main():

    
    alunos_notas = []   

    medias = []

    alunos = int(input("quantos alunos vao ser inseridos:"))

    aux = 0

    for i in range(alunos):
        print("\n")
        notas = [int(input(f"{j + 1}° nota do {i + 1}° aluno:"))for j in range(4)]

        media = sum(notas)/ 4        
        medias.append(media)

        alunos_notas.append(notas)
            

    print(alunos_notas)
    print("\n")
    print(medias)

main()