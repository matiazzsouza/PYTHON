# exercicios 6 e 7 juntos 


def celsius ():

    print("\n")
    print("deseja converter de celsius para qual escala?")
    print("1-)fahrenheint\n2-)kelvin\n3-)Rankine\n4-)Réaumur\n5-)voltar ao menu\n")
    test = int(input("Digite o número da escala que deseja converter\n"))
    
    if(test == 1):
        celsius = float(input("Digite a temperatura em celsius: "))
        fahrenheint = (celsius * 9/5) + 32
        print(f"A temperatura em fahrenheint é: {fahrenheint}")
        menu()
        
    elif test == 2:
        celsius = float(input("Digite a temperatura em celsius: "))
        kelvin = celsius + 273.15
        print(f"A temperatura em kelvin é: {kelvin}")
        menu()
        
    elif test == 3:
        celsius = float(input("Digite a temperatura em celsius: "))
        rankine = (celsius + 273.15) * 9/5
        print(f"A temperatura em rankine é: {rankine}")
        menu()
        
    elif test == 4:
        celsius = float(input("Digite a temperatura em celsius: "))
        reaumur = celsius * 4/5
        print(f"A temperatura em reaumur é: {reaumur}")
        menu()
        
    elif test == 5:
        menu()

    else:    
        print("Opção inválida")
        celsius()

def fahrenheint ():
    
    print("\n")
    print("deseja converter de fahrenheint para qual escala?")
    print("1-)celsiu\n2-)kelvin\n3-)Rankine\n4-)Réaumur\n5-)voltar ao menu\n")
    test = int(input("Digite o número da escala que deseja converter\n"))
    
    if(test == 1):
        fahrenheint = float(input("Digite a temperatura em fahrenheint: "))
        celsius = (fahrenheint - 32) * 5/9
        print(f"A temperatura em celsius é: {celsius}")
        menu()
        
    elif test == 2:
        fahrenheint = float(input("Digite a temperatura em fahrenheint: "))
        kelvin = (fahrenheint - 32) * 5/9 + 273.15
        print(f"A temperatura em kelvin é: {kelvin}")
        menu()
        
    elif test == 3:
        fahrenheint = float(input("Digite a temperatura em fahrenheint: "))
        rankine = fahrenheint + 459.67
        print(f"A temperatura em rankine é: {rankine}")
        menu()
        
    elif test == 4:
        fahrenheint = float(input("Digite a temperatura em fahrenheint: "))
        reaumur = (fahrenheint - 32) * 4/9
        print(f"A temperatura em reaumur é: {reaumur}")
        menu()
        
    elif test == 5:
        menu()

    else:    
        print("Opção inválida")
        fahrenheint()

def kelvin ():
    
    print("\n")
    print("deseja converter de kelvin para qual escala?")
    print("1-)celsiu\n2-)fahrenheint\n3-)Rankine\n4-)Réaumur\n5-)voltar ao menu\n")
    test = int(input("Digite o número da escala que deseja converter\n"))
    
    if(test == 1):
        kelvin = float(input("Digite a temperatura em kelvin: "))
        celsius = kelvin - 273.15
        print(f"A temperatura em celsius é: {celsius}")
        menu()
        
    elif test == 2:
        kelvin = float(input("Digite a temperatura em kelvin: "))
        fahrenheint = (kelvin - 273.15) * 9/5 + 32
        print(f"A temperatura em fahrenheint é: {fahrenheint}")
        menu()
        
    elif test == 3:
        kelvin = float(input("Digite a temperatura em kelvin: "))
        rankine = kelvin * 9/5
        print(f"A temperatura em rankine é: {rankine}")
        menu()
        
    elif test == 4:
        kelvin = float(input("Digite a temperatura em kelvin: "))
        reaumur = (kelvin - 273.15) * 4/5
        print(f"A temperatura em reaumur é: {reaumur}")
        menu()
        
    elif test == 5:
        menu()

    else:    
        print("Opção inválida")
        kelvin()

def rankine ():
    
    print("\n")
    print("deseja converter de rankine para qual escala?")
    print("1-)celsiu\n2-)fahrenheint\n3-)kelvin\n4-)Réaumur\n5-)voltar ao menu\n")
    test = int(input("Digite o número da escala que deseja converter\n"))
    
    if(test == 1):
        rankine = float(input("Digite a temperatura em rankine: "))
        celsius = (rankine - 491.67) * 5/9
        print(f"A temperatura em celsius é: {celsius}")
        menu()
        
    elif test == 2:
        rankine = float(input("Digite a temperatura em rankine: "))
        fahrenheint = rankine - 459.67
        print(f"A temperatura em fahrenheint é: {fahrenheint}")
        menu()
        
    elif test == 3:
        rankine = float(input("Digite a temperatura em rankine: "))
        kelvin = rankine * 5/9
        print(f"A temperatura em kelvin é: {kelvin}")
        menu()
        
    elif test == 4:
        rankine = float(input("Digite a temperatura em rankine: "))
        reaumur = (rankine - 491.67) * 4/9
        print(f"A temperatura em reaumur é: {reaumur}")
        menu()
        
    elif test == 5:
        menu()

    else:    
        print("Opção inválida")
        rankine()

def reaumur ():
    
    print("\n")
    print("deseja converter de reaumur para qual escala?")
    print("1-)celsiu\n2-)fahrenheint\n3-)kelvin\n4-)Rankine\n5-)voltar ao menu\n")
    test = int(input("Digite o número da escala que deseja converter\n"))
    
    if(test == 1):
        reaumur = float(input("Digite a temperatura em reaumur: "))
        celsius = reaumur * 5/4
        print(f"A temperatura em celsius é: {celsius}")
        menu()
        
    elif test == 2:
        reaumur = float(input("Digite a temperatura em reaumur: "))
        fahrenheint = reaumur * 9/4 + 32
        print(f"A temperatura em fahrenheint é: {fahrenheint}")
        menu()
        
    elif test == 3:
        reaumur = float(input("Digite a temperatura em reaumur: "))
        kelvin = reaumur * 5/4 + 273.15
        print(f"A temperatura em kelvin é: {kelvin}")
        menu()
        
    elif test == 4:
        reaumur = float(input("Digite a temperatura em reaumur: "))
        rankine = reaumur * 9/4 + 491.67
        print(f"A temperatura em rankine é: {rankine}")
        menu()
        
    elif test == 5:
        menu()

    else:    
        print("Opção inválida")
        reaumur()


def menu():

    print("\n")
    print("\t\t\tMENU")
    print("\tEscolha a temperatura que deseja converter:\n")
    test = int(input("0-)celsiu\n1-)fahrenheint\n2-)kelvin\n3-)Rankine\n4-)Réaumur\n5-)sair\nDigite o número da escala que deseja converter\n"))
    if(test == 0):
        celsius()
    if test == 1:
        fahrenheint()
    elif test == 2:
        kelvin()
    elif test == 3:
        rankine()
    elif test == 4:
        reaumur()
    elif test == 5:
        print("Obrigado por usar o conversor de temperatura") 
    else:    
        print("Opção inválida")
        menu()


def main():
    
    print("\n")
    print("-"*50)
    print("  OLA SEJA BEM-VINDO AO CONVERSOR DE TEMPERATURA")
    print("-"*50)
    print("      aperte enter para continuar...\n")
    input()

    menu()


main()