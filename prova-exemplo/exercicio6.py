import os

def limpar_tela():
    # Para Windows
    if os.name == 'nt':
        os.system('cls')
        

def main():

    i = 0
    j = 1

    cont = 0
    contn = 0

    soma = 0
    somap = 0

    maior = 0
    menor = 9999

    maiorp = 0
    menorp = 9999


    while(j == 1):

        i += 1

        print("\n")
        print(f"{i}°Paciente:")
        age = int(input("digite a sua idade:"))

        if(age > maior):
            maior = age
        
        if(age < menor):
            menor = age
        
        soma += age

        peso = float(input("digite o seu peso:"))

        if(peso > maiorp):
            maiorp = age
        
        if(peso < menorp):
            menorp = age
        
        somap += age
    

        exe = input("Faz exercicio (S/N):")

        if(exe == "S" or exe == "s"):
            cont += 1

        else:
            contn += 1
        

        j = int(input("\nDeseja anotar outro paciente?\n1-Sim\n2-Não"))
        
        
    limpar_tela()
    print(f"numero de intrevistas:{i}")
    print("-"*50)
    print(f"idade media:{soma / i}")
    print(f"maior idade:{maior}")
    print(f"menor idade:{menor}")
    print(f"peso medio:{somap / i}")
    print(f"maior peso:{maiorp}")
    print(f"menor peso:{menorp}")
    print(f"Pessoas que treinam:{cont}")
    print(f"Pessoas que nao treinam:{contn}")
    print("-"*50)


main()