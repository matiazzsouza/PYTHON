import os

def limpa():
    
    if os.name == 'nt':
        os.system('cls')

def base():

    dados = []

    return dados

def altera(dados):

    limpa()

    rep = 0  

    while(True):
        limpa()
        id = int(input("Digite o id do produto:"))
        for i in range(len(dados)):
            if(id == dados[i][0]):
                print("-" * 82)
                print(f"| 1-{'Produto':<5} | 2-{'Estoque':^6} | 3-{'Vendidos':^10} | 4-{'Preço unitario':^9} | 5-{'Impostos(%)':^10} |")
                print("-" * 82)

                for j in range(5):
                    if (j == 1):  
                        print(f"|{dados[i][j]:<5}", end=" | ")
                    elif (j == 2):
                        print(f"{dados[i][j]:^6}", end=" | ")
                    elif (j == 3):  
                        print(f"{dados[i][j]:^10}", end=" | ")
                    elif (j == 4):  
                        print(f"{dados[i][j]:^9}", end=" | ")
                    elif (j == 5):  
                        print(f"{dados[i][j]:^10}", end=" | ")

                print()  # Pular linha 
                print("-" * 82)

                while(True):
                    opc = int(input("Digite o número da informação que quer mudar:"))
                    
                    if(opc == 1):
                        muda = input("Digite o novo nome do produto:")#nome
                    
                    elif(2 <= opc <= 5):
                        muda = int(input("Digite o novo valor:"))
                    
                    else:
                        input("Número de opção invalida, aperte enter e digite novamente")
                        continue

                    dados[i][opc] = muda
                    input("Informação alterada com sucesso, aperte enter para voltar ao menu...")
                    return

                rep += 1
                if rep == 3:
                    input("Não está encontrando o produto, volte ao menu e escolha a opção 2...")
                    return

                input("Produto não consta na base de dados ou número de ID errado, aperte enter para digitar novamente...")

def deleta(dados):


    rep = 0 

    while(True):
        limpa()
        ids = int(input("Digite o número de ID do produto:"))
        for i in range(len(dados)):
            if(ids == dados[i][0]):
                dele = int(input(f"Tem certeza que quer apagar o produto: {dados[i][1].upper()}\n1)Sim\n2)Não"))
                if(dele != 1):
                    limpa()
                    input("Ok, aperte enter que voltara para o menu")
                    return
                del dados[i]
                input("Produto apagado com sucesso, aperte enter para voltar ao menu...")
                return
        
            if(rep == 3):
                input("Não esta encontrando o produto, volte ao menu e escolha a opção 2...")
                return

            rep += 1
            input("Produto não consta na base de dados ou número de ID errado, aperte enter para digitar novamente...")

def consultaNome(dados):

    limpa()

    rep = 0

    while(True):
        limpa()
        nome = input("Digite o nome do produto:")
        for i in range(len(dados)):
            if(nome == dados[i][1]):
                print("-" * 82)
                print(f"|{'ID':<15} | {'Produto':<5} | {'Estoque':^6} | {'Vendidos':^10} | {'Preço unitario':^9} | {'Impostos(%)':^10} |")
                print("-" * 82)

                for j in range(6):
                    if (j == 0): 
                        print(f"|{dados[i][j]:<15}", end=" | ")
                    elif (j == 1):  
                        print(f"{dados[i][j]:<5}", end=" | ")
                    elif (j == 2):
                        print(f"{dados[i][j]:^6}", end=" | ")
                    elif (j == 3):  
                        print(f"{dados[i][j]:^10}", end=" | ")
                    elif (j == 4):  
                        print(f"{dados[i][j]:^9}", end=" | ")
                    elif (j == 5):  
                        print(f"{dados[i][j]:^10}", end=" | ")

                print()  # Pular linha 
                print("-" * 82)
                input("aperte enter para voltar ao menu...")
                return

            if(rep == 3):
                input("Não esta encontrando o produto, volte ao menu e escolha a opção 2...")  
                return

            rep += 1
            input("Produto não consta na base de dados ou número de ID errado, aperte enter para digitar novamente...")

def consulta(dados):

    limpa()

    rep = 0

    while(True):
        cons = int(input("Digite o ID do produto:"))
        for i in range(len(dados)):
            if(cons == dados[i][0]):
                print("-" * 82)
                print(f"|{'ID':<15} | {'Produto':<5} | {'Estoque':^6} | {'Vendidos':^10} | {'Preço unitario':^9} | {'Impostos(%)':^10} |")
                print("-" * 82)

                for j in range(8):
                    if (j == 0): 
                        print(f"|{dados[i][j]:<15}", end=" | ")
                    elif (j == 1):  
                        print(f"{dados[i][j]:<5}", end=" | ")
                    elif (j == 2):
                        print(f"{dados[i][j]:^6}", end=" | ")
                    elif (j == 3):  
                        print(f"{dados[i][j]:^10}", end=" | ")
                    elif (j == 4):  
                        print(f"{dados[i][j]:^9}", end=" | ")
                    elif (j == 5):  
                        print(f"{dados[i][j]:^10}", end=" | ")

                print()  # Pular linha 
                print("-" * 82)
                input("aperte enter para voltar ao menu...")
                return

        rep += 1
        if(rep == 3):
            input("Não esta encontrando o produto, volte ao menu e escolha a opção 2...")  
            return

        input("Produto não consta na base de dados ou número de ID errado, aperte enter para digitar novamente...")

def cadastrar(dados, id):

    limpa()

    qnt = int(input("Quantos produtos deseja digitar:"))

    for i in range(qnt):
        limpa()
        id += 1
        prod = input("Nome do produto:")
        prod = prod.lower()
        est = int(input("Quantidade em estoque:"))
        venda = int(input("Quantidade de vendas:"))      
        preco = float(input("Digite o preço do produto:"))
        porc = float(input("Porcentual de imposto:"))
        porc = porc / 100
        produtos = [id, prod, est, venda, preco, porc]

        dados.append(produtos)
        print()
        input("Produto cadastrado com sucesso!!")

    return id

def tabela(dados):

    
    limpa()

    print("-" * 82)
    print(f"|{'ID':<15} | {'Produto':<5} | {'Estoque':^6} | {'Vendidos':^10} | {'Preço unitario':^9} | {'Impostos(%)':^10} |")
    print("-" * 82)


    for i in range(len(dados)):
        for j in range(6):
            if (j == 0): 
                print(f"|{dados[i][j]:<15}", end=" | ")
            elif (j == 1):  
                print(f"{dados[i][j]:<5}", end=" | ")
            elif (j == 2):  
                print(f"{dados[i][j]:^6}", end=" | ")
            elif (j == 3):  
                print(f"{dados[i][j]:^10}", end=" | ")
            elif (j == 4):  # Peso
                print(f"{dados[i][j]:^9}", end=" | ")
            elif (j == 5):  # Pressão
                print(f"{dados[i][j]:^10}", end=" | ")

        print()  # Pular linha 
        print("-" * 82)
    

    input("\nAperte ent para continuar...")

    return

def relatorios(dados):


    rep = 0

    limpa()
    while(True):
        ids = int(input("Digite o id do produto para ver o relatorio:"))
        for i in range(len(dados)):
            if(ids == dados[i][0]):
                print("realtorios:")

                return
                
            rep += 1
            if(rep == 3):
                input("Não esta encontrando o produto, volte ao menu e escolha a opção 2...")  
                return

            input("Produto não consta na base de dados ou número de ID errado, aperte enter para digitar novamente...")


def ler():

    dados = base()
    id = 0

    while(True):
        while(True):
            limpa()
            print("1)Cadastrar produto\n2)Listar produtos\n3)Consultar produto por ID\n4)Consultar produto pelo nome\n5)Alterar produto\n6)Deletar produto\n7)Relatorio dos produtos\n8)Sair")

            opc = int(input("Escolha alguma das opções acima:"))

            if(opc == 1):
                id = cadastrar(dados, id)
                continue
            
            elif(opc == 2):
                if(len(dados) == 0):
                    limpa()
                    input("Base de dados vazia, aperte enter para voltar ao menu...")
                    continue
                tabela(dados)
            
            elif(opc == 3):
                if(len(dados) == 0):
                    limpa()
                    input("Base de dados vazia, aperte enter para voltar ao menu...")
                    continue
                consulta(dados)

            elif(opc == 4):
                if(len(dados) == 0):
                    limpa()
                    input("Base de dados vazia, aperte enter para voltar ao menu...")
                    continue
                consultaNome(dados)
            
            elif(opc == 5):
                if(len(dados) == 0):
                    limpa()
                    input("Base de dados vazia, aperte enter para voltar ao menu...")
                    continue
                altera(dados)
            
            
            elif(opc == 6):
                if(len(dados) == 0):
                    limpa()
                    input("Base de dados vazia, aperte enter para voltar ao menu...")
                    continue
                deleta(dados)

            elif(opc == 7):
                if(len(dados) == 0):
                    limpa()
                    input("Base de dados vazia, aperte enter para voltar ao menu...")
                    continue
                relatorios(dados)            

            elif(opc == 8):
                limpa()
                return

def main():

    print("BEM-VINDO AO ROMA")
    input("Aperte enter para continuar...")


    ler()

    print("Obrigado por acessar o ROMA")



main()
