import random


def main():


    num = 0 
    im = 0
    ip = 0


    print("-"*80)
    print("\t\tSEJÁ BEM-VINDO AO JOKENPO VIRTUAL")
    print("-"*80)
    print("\t\taperte enter para iniciar...")
    input()


    while(ip + im != 3):
        print("\n")
        escolha = random.randint(1, 3)
        print(f"{escolha:.2f}")
        num = int(input("escolha entre:\n1-Pedra\n2-Papel\n3-Tesoura\n"))

        if(num > 3 or num < 1):
            print("\nnumero invalido, digite novamente!!\n")

        if(num == 1 and escolha == 2):      #PEDRA
            print("VOCÊ ESCOLHEU PEDRA")
            print("PAPEL <-- PEDRA\nPERDEUUUU")
            im += 1

        elif(num == 1 and escolha == 3):
            print("VOCÊ ESCOLHEU PEDRA")
            print("PEDRA <-- TESOURA\nGANHOUUUU")
            ip += 1

        if(num == 2 and escolha == 1):      #PAPEL
            print("VOCÊ ESCOLHEU PAPEL")
            print("PAPEL <-- PEDRA\nGANHOUUUU")
            ip += 1

        elif(num == 2 and escolha == 3):
            print("VOCÊ ESCOLHEU PAPEL")
            print("TESOURA <-- PAPEL\nPERDEUUU")
            im +=1

        if(num == 3 and escolha == 1):      #TESOURA
            print("VOCÊ ESCOLHEU TESOURA")
            print("PEDRA <-- TESOURA\nPERDEUUUU")
            im +=1 

        elif(num == 3 and escolha == 2):
            ip += 1
            print("VOCÊ ESCOLHEU TESOURA")
            print("TESOURA <-- PAPEL\nGANHOUUU")

        if(num == escolha):  #CASO O USUARIO JOGUE O MESMO NUMERO QUE O COMPUTADOR ELE IRA REINICIAR IGUAL NA VIDA REAL
            print("EMPATOUUUUU, ESCOLHA NOVAMENTE:\n")
            
        print("\n")
        print("-"*60)
        print("PONTUAÇÃO:")
        print(f"MAQUINA = {im}")
        print(f"JOGADOR = {ip}")
        print("-"*60)
    
    if(ip > im):
        print("JOGADOR VENCEU")
    elif(ip < im):
        print("MAQUINA VENCEU")

    print("\n")

main()