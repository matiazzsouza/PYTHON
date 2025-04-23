import os

def limpar_tela():
    # Para Windows
    if os.name == 'nt':
        os.system('cls')

    return


def base():


    return []
    

def exibir_dados(dados):
    
    limpar_tela()
    
    if (len(dados) != 0):
        for i in dados:
            print(i)
    else:
        print("Base de dados está vazia.")


def remove(dados):

    remCPF = input("\nDigite o CPF do usuario que deseja apagar:\n")
    encontrado = True

    for i in range(len(dados)):
        if(remCPF == dados[i][2]):
            print(f"Usuario {dados[i][0]} deletado do banco de dados")
            del dados[i]
            encontrado = True
            break

    if not encontrado:
        print("CPF não encontarado")
    
    return


def inserir(dados):

    tam = int(input("Quantas linhas voce deseja inserir"))

    for i in range(tam):
        print(f"\n{i + 1}° linha:")
        nome = input("Digite o nome:")
        cpf = input("Digite o cpf:")
        idade = int(input("Digite a idade:"))
        cadastro = [nome,idade,cpf]
        dados.append(cadastro)

    return

def ler(dados):
    
    while True:
        opcao = int(input("Digite a opção que você deseja:\n1)Ver a base de dados\n2)Inserir dados\n3)Remover dados\n4)Alterar dados\n5)Sair "))

        if (opcao == 1):
            exibir_dados(dados)

        elif (opcao == 2):
            inserir(dados)

        elif (opcao == 3):
            remove(dados)

        elif (opcao == 4):
            altera(dados)

        elif (opcao == 5):
            break
        else:
            print("\nOpção inválida. Tente novamente.")
            limpar_tela()
            continue

        volta = int(input("\nDeseja fazer mais algo?\n1)Sim\n2)Não\n"))

        if volta != 1:
            break
        limpar_tela()

def main():


    
    print("\t\t\nBem-Vindo ao Banco de dados\n\taperte enter para continuar...")

    input()

    limpar_tela()

    dados = base()

    ler(dados)

    limpar_tela()
    print("\nObrigado por acessar o site")



main()