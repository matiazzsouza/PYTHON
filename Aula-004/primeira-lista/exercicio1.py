def sistema(name, senha, age):
    print("\n------------------------------------------------------")
    print(f"\t\tOLÁ SEJA BEM-VINDO {name.upper()}")
    print("------------------------------------------------------\n")
    print("\tAPERTE ENTER PARA CONTINUAR...")
    input()

    print("SUAS INFORMAÇÕES:")
    print(f"Nome: {name}") 
    print(f"Idade: {age}")
    print(f"Senha: {senha}")
    
    return

def entrar(name, senha, age):
    name_test = input("\nDigite o nome do cliente: ")
    senha_test = input("Digite a senha do cliente: ")

    if (name_test == name and senha_test == senha):
        print("\nEntrando no sistema...")
        sistema(name, senha, age)
    else:
        print("\nNome ou senha incorretos!")
        print("\nTente novamente...")
        entrar(name, senha, age)  # Passamos os parâmetros novamente
    
    return

def cadastro():
    name = input("\nDigite o nome do cliente: ")
    age = int(input("\nDigite a idade do cliente: "))
    senha = input("\nDigite a senha do cliente: ")
    confirm_senha = input("Confirme a senha do cliente: ")

    if (senha == confirm_senha):
        print("\nCadastro realizado com sucesso!")
        main(name, senha, age)  # Agora passamos os dados para o main()
    else:
        print("\nAs senhas não coincidem!")    
        print("\nTente novamente...")
        cadastro()
    
    return

def main(name = None, senha = None, age = 0):
    print("\n------------------------------------------------------")
    print("OLA SEJA BEM-VINDO AO SISTEMA DE CADASTRO DE CLIENTES")
    print("------------------------------------------------------\n")
    print("\tAPERTE ENTER PARA CONTINUAR...")
    input()

    test = int(input("Digite 1 para entrar ou 2 para cadastrar: "))

    if (test == 1):
        if name and senha:  # Verifica se já existe um cadastro
            entrar(name, senha, age)  # Passamos os dados cadastrados
        else:
            print("\nNenhum usuário cadastrado! Faça um cadastro primeiro.")
            cadastro()
    
    elif (test == 2):
        cadastro()

main()  
