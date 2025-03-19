import random


#TODOS OS EXERCICIOS SOBRE O JOGO ESTÃO NESSE ARQUIVO DE 7 A 10

def reinicia(numale):

        num2 = int(input("DESEJA DESISTIR ??\n1-)sim\n2-)não\n"))
            
        if(num2 == 1):

            print("\n")
            print("-"*60)
            print("\t\tOBRIGADO POR JOGAR, VOLTE SEMPRE!!!")
            print("-"*60)
            
            num = numale #passando o valor do numero aleatorio para acabar com o jogador deseje parar de jogar
            
            num3 = int(input("\n\nDESEJA INICIAR UM JOGO NOVO??\n1-)SIM\n2-)NÃO\n"))
            
            if(num3 != 1):
                return num
            else:
                main()

        else:
            return

def main():

    print("\n")
    print("-"*60)
    print("\t\tBEM-VINDO AO JOGO DO NUMERO ALEATORIO")
    print("-"*60)
    print("\t\taperte enter para continuar...")
    input()

    numale = random.randint(0 , 100)

    i = 1

    num = 0
    num2 = 0

    while(num != numale):
        
        print(f"\n{i}° tentativa")
        
        num = int(input("tente acertar o numero:"))

        i+=1

        if(num > numale):
            print("MENOR\n")

        elif(num < numale):
            print("MAIOR\n")

        else: 
            print("\n\nPARABENS VOCÊ GANHOUUUU\n\n")

        num = reinicia(numale)

main()
