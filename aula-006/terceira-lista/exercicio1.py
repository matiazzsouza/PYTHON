import os

def limpa():
    
    if os.name == 'nt':
        os.system('cls')

def base():

    dados = [

    ]

    return dados

def tabela(dados):

    limpa()

    qnt = len(dados)


    print("-" * 105)
    print(f"|{'Nome':<15} | {'Idade':<5} | {'Sexo':^6} | {'Altura(m)':^10} | {'Peso(kg)':^9} | {'Pressão':^10} | {'Tipo Sanguíneo':^15} | {'Cardiologia':^12}|")
    print("-" * 105)


    for i in range(qnt):
        for j in range(8):
            if (j == 0): 
                print(f"|{dados[i][j]:<15}", end=" | ")
            elif (j == 1):  # Idade
                print(f"{dados[i][j]:<5}", end=" | ")
            elif (j == 2):  # Sexo
                print(f"{dados[i][j]:^6}", end=" | ")
            elif (j == 3):  # Altura
                print(f"{dados[i][j]:^10}", end=" | ")
            elif (j == 4):  # Peso
                print(f"{dados[i][j]:^9}", end=" | ")
            elif (j == 5):  # Pressão
                print(f"{dados[i][j]:^10}", end=" | ")
            elif (j == 6):  # Tipo Sanguíneo
                print(f"{dados[i][j]:^15}", end=" | ")
            elif (j == 7):  # Cardiologia
                print(f"{dados[i][j]:^12}", end=" | ")

        print()  # Pular linha depois de cada paciente
        print("-" * 105)
    

    input("\nAperte ent para continuar...")

    return

def deletar(dados):


    limpa()

    rep = 0

    while(True):
        nomedel = input("Digite o nome do paciente:")
        for i in range(len(dados)):
            if(nomedel == dados[i][0]):
                opc = int(input("Tem certeza que deseja apagar esse paciente:\n1)Sim\n2)Não"))

                if(opc != 1):
                    print("Ok, volte ao menu e escolha opção que deseja:")
                    return

                del dados[i]
                print("Paciente deletado com sucesso")
                return

        print("Paciente não encontrado, digite o nome novamente")
        rep += 1

        if(rep > 3):
            print("Não esta encontrando o nome do paciente, volte ao menu e escolha a opção 1")
            return

def consulta(dados):

    rep = 0


    while(True):
        limpa()
        for i in range(len(dados)):
            nome = input("Digite o nome do paciente:")
            if(nome == dados[i][0]):

                print("-" * 105)
                print(f"|{'Nome':<15} | {'Idade':<5} | {'Sexo':^6} | {'Altura(m)':^10} | {'Peso(kg)':^9} | {'Pressão':^10} | {'Tipo Sanguíneo':^15} | {'Cardiologia':^12}|")
                print("-" * 105)

                for j in range(8):
                    if (j == 0): 
                        print(f"|{dados[i][j]:<15}", end=" | ")
                    elif (j == 1):  # Idade
                        print(f"{dados[i][j]:<5}", end=" | ")
                    elif (j == 2):  # Sexo
                        print(f"{dados[i][j]:^6}", end=" | ")
                    elif (j == 3):  # Altura
                        print(f"{dados[i][j]:^10}", end=" | ")
                    elif (j == 4):  # Peso
                        print(f"{dados[i][j]:^9}", end=" | ")
                    elif (j == 5):  # Pressão
                        print(f"{dados[i][j]:^10}", end=" | ")
                    elif (j == 6):  # Tipo Sanguíneo
                        print(f"{dados[i][j]:^15}", end=" | ")
                    elif (j == 7):  # Cardiologia
                        print(f"{dados[i][j]:^12}", end=" | ")

                print()  # Pular linha depois de cada paciente
                print("-" * 105)

                input("\nAperte ent para voltar ao menu...")
                return

            else:  
                rep += 1
                
                if(rep > 3):
                    input("Não está achando o paciente, volte ao menu e selecione a opção de número 1")
                
                    return

                input("Paciente não encontrado, aperte enter para digitar novamente ")
                continue

def alterar(dados):

    limpa()

   
    rep = 0
    
    while(True):
        limpa()
        for i in range(len(dados)): 
            nomealt = input("Qual o nome do paciente:")
            nomealt = nomealt.lower()
            if(nomealt == dados[i][0]): 

                print("-" * 105)
                print(f"|{'1-Nome':<15} | {'2-Idade':<5} | {'3-Sexo':^6} | {'4-Altura(m)':^10} | {'5-Peso(kg)':^9} | {'6-Pressão':^10} | {'7-Tipo Sanguíneo':^15} | {'8-Cardiologia':^12}|")
                print("-" * 105)
                
                for j in range(8):
                    if (j == 0): 
                        print(f"|{dados[i][j]:<15}", end=" | ")
                    elif (j == 1):  # Idade
                        print(f"{dados[i][j]:<5}", end=" | ")
                    elif (j == 2):  # Sexo
                        print(f"{dados[i][j]:^6}", end=" | ")
                    elif (j == 3):  # Altura
                        print(f"{dados[i][j]:^10}", end=" | ")
                    elif (j == 4):  # Peso
                        print(f"{dados[i][j]:^9}", end=" | ")
                    elif (j == 5):  # Pressão
                        print(f"{dados[i][j]:^10}", end=" | ")
                    elif (j == 6):  # Tipo Sanguíneo
                        print(f"{dados[i][j]:^15}", end=" | ")
                    elif (j == 7):  # Cardiologia
                        print(f"{dados[i][j]:^12}", end=" | ")

                print() 
                print("-" * 105)

                muda = int(input("\nDigite o número da opção que voce deseja mudar:"))
                
                if(muda > 8):
                    input("Opção invalida, aperte enter para digitar novamente...")
                    continue

                muda -= 1

                dados[i][muda] = ""
                novo = input("Digite a nova informação:")

                if(muda == 6):
                    novo = novo.upper()

                dados[i][muda] += novo
                input("Informação mudada com sucesso, aperte enter para voltar ao menu")
                return
        
            else:
                rep += 1
                if(rep > 3):
                    input("Não esta encontrando o paciente aperte enter para ir ao menu e escolha a opção de número 1")
                    return

                input("Nome do paciente não encontrado, digite novamnte...")
                continue

def cadastro(dados):

    limpa()
    qnt = int(input("Quantos pacientes você deseja cadastrar:"))

    pac = []

    for i in range(qnt):
        limpa()
        nome = input("Digite o nome do paciente:")
        nome = nome.lower()
        idade = input("Digite a idade do paciente:")
        sexo = input("Digite o sexo do paciente(M/F):")
        altura = input("Digite a altura do paciente(Cm):") 
        peso = input("Digite o peso do paciente(Kg):")
        pressao = input("Pressão do paciente:")
        sangue  = input("Tipo sanguinieo:")
        sangue = sangue.upper()

        cardio = input("Possui algum tipo de comorbidade cardiaca(S/N):")

        pac = [nome,idade,sexo,altura,peso,pressao,sangue,cardio]

        dados.append(pac)
        print()
        print("Paciente cadastrado com sucesso")
        input()
        
def ler():

    dados = base()

    limpa()
    
    print("\tBEM-VINDO A CeCaR\n  aperte enter para continuar...")
    input()

    while(True):
        while(True):
            limpa() 
            print("Quais opções você deseja escolher:\n")
            print("1)Ver dados cadastrados\n2)Cadastrar paciente\n3)Consultar paciente\n4)Deletar paciente pelo nome\n5)Alterar dados do paciente\n6)Sair")

            opcao = int(input())

            if(opcao == 1):
                if(len(dados) == 0):
                    limpa()

                    print("Base dados vazia, aperte enter para voltar ao menu..." )
                    input()

                    limpa()
                    continue

                else:
                    tabela(dados)
                    break
            
            elif(opcao == 2):
                cadastro(dados)
                break
                
            elif(opcao == 3):
                consulta(dados)
                break

            elif(opcao == 4):
                deletar(dados)
                break
            
            elif(opcao == 5):
                alterar(dados)
                break

            elif(opcao == 6):
                return
            
            limpa()

def main():

    ler()

    limpa()
    print("obrigado por acessar o CeCaR")

main()