import random



def main():

    print("-"*60)
    print("\t\tBEM-VINDO AO JOGO DO NUMERO ALEATORIO")
    print("-"*60)
    print("\t\taperte enter para continuar...")
    input()

    numale = random.randint(0 , 100)

    i = 0

    num = 0

    while(num != numale):
        num = int(input("tente acertar o numero:"))
        
        i+=1

        print(f"{i}° tentativa")

        if(num > numale):
            print("MENOR\n")

        elif(num < numale):
            print("MAIOR\n")

        else: 
            print("IGUAL")


main()
