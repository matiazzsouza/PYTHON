import os 
def limpa():
    os.system("cls")

def base():

    return {}

def lista(dados):
    
    for i in dados:
        print(f"{i} - {dados[i]}\n")

    input("Aperte enter para voltar ao menu...")
        
def consultar(dados):

    cont = 0

    while True:
        nome = input("Digite o nome que deseja consultar:").lower()

        if nome in dados:
            print(nome, dados[nome])
            input("Aperte enter para voltar ao menu...")
            break
        else:
            input("Nome do usuario não encontrado,aperte enter e digite novamente")
            cont += 1
            if(cont == 3):
                input("Caso não esteja lembrando nome do usuario volte ao menu e escolha a opção 1")
                break
            limpa()
            
def deletar(dados):

    nome = input("Digite o nome que deseja deletar:").lower()

    if nome in dados:
        try:
            print("Usuario encontrado")
            opc = int(input("\nDeseja mesmo deletar esse usuario:\n1)Sim\n2)Não"))
            if(opc == 1):
                del dados[nome]
            else:
                input("aperte enter para voltar ao menu...")
        except:
            input("Caractere não numerico,aperte enter para digitar novamnte...")

def cadastrar(dados):


    print("Cadastre um novo usuario")

    nome = input("\nDigite o nome do usuario:").lower()

    if nome in dados:
        input("Nome ja adicionado, escolha novamnte essa opcao e escreva outro nome")
        return

    telefone = input("Digite o número de telefone:")
    email = input("Digite o email:").lower()

    while True:
        try:
            altura = float(input("Digite a altura(M):"))
            peso = float(input("Digite o peso(Kg):"))
            break
        except:
            print("Caractere digitado não númerico")

    dados[nome] = {"telefone": telefone, "email": email, "altura": altura, "peso":peso}

def alterar(dados):

    cont = 0

    while True:
        nome = input("Digite o nome do usuario:")

        if nome in dados:
            print("Usuario encontrado\n")
            print("Qual das informações voce deseja mudar:")
            print("1)Nome")
            print("2)Telefone")
            print("3)Email")
            print("4)Altura")
            print("5)Peso")
            try:
                opc = int(input())
            except:
                input("Caractere não numerico, digite nomente")
            
            chaves = ["nome", "telefone", "email", "altura", "peso"]
            campo = chaves[opc - 1]

            if(opc == 1):
                nvnome = input("Digite o novo nome:")
                dados[nvnome] = dados.pop(nome)
                nome = nvnome
                input("Nome mudado com sucesso, aperte enter para ir ao menu...")
                return

            if(opc > 3):
                try:
                    nvinfo = float(input("Digite a nova informação:"))
                    dados[nome][campo] = nvinfo
                except ValueError:
                    print("caractere nao numerico")

            else:    
                nvinfo = input("Digite a nova informação:")

                dados[nome][campo] = nvinfo
                


            input("\nNova informação adicionada com sucesso, aperte enter para voltar ao menu...")
            break

        else:
            cont += 1

            if(cont == 3):
                input("Não esta achando o usuario, volte ao menu e escolha a opção 1")
                return

            input("Usuário não encontrado. Pressione Enter para digitar novamente")
            limpa()

def  imc(dados):

    cont = 0
    
    while True:
        limpa()
        nome = input("Digite o nome do usuario:")

        if nome in dados:
            print("\nUsuario encontrado\n")
            imc = dados[nome]["peso"] / dados[nome]["altura"] ** 2
            if imc < 18.5:
                print(f"O IMC do usuario {nome} é: {imc:.2f}\nSituação atual: Abaixo do peso ")

            elif 18.5 < imc < 24.9:
                print(f"O IMC do usuario {nome} é: {imc:.2f}\nSituação atual: Peso normal ")

            elif 25 < imc < 29.9:
                print(f"O IMC do usuario {nome} é: {imc:.2f}\nSituação atual: Sobrepeso ")

            elif 30 < imc < 34.9:
                print(f"O IMC do usuario {nome} é: {imc:.2f}\nSituação atual: Obesidade grau 1 ")

            elif 35 < imc < 39.9:
                print(f"O IMC do usuario {nome} é: {imc:.2f}\nSituação atual: Obesidade grau 2 ")

            elif imc > 40:
                print(f"O IMC do usuario {nome} é: {imc:.2f}\nSituação atual: Obesidade grau 3 ")
            
            input("\nAperte enter para voltar ao menu...")
            return

        else:
            cont += 1
            if(cont == 3):
                input("Não esta encontrando o usuario, aperte enter para voltar ao menu e escolha a opção 1")
                return

            input("Usuario nao encontrado, aperte enter para digitar novamente")

def estatisticas(dados):


    maior_altura = 0
    menor_altura = float("inf")
    nome_maior_altura = ""
    nome_menor_altura = ""

    maior_peso = 0
    menor_peso = float("inf")
    nome_maior_peso = ""
    nome_menor_peso = ""

    peso_med = 0
    alt_med = 0

    nome_mais_longo = ""
    nome_mais_curto = ""

    maior_imc = 0
    menor_imc = float("inf")
    nome_maior_imc = ""
    nome_menor_imc = ""

    for nome in dados:
        peso = dados[nome]["peso"]
        altura = dados[nome]["altura"]
        imc = peso / (altura ** 2)

        # IMC
        if imc > maior_imc:
            maior_imc = imc
            nome_maior_imc = nome

        if imc < menor_imc:
            menor_imc = imc
            nome_menor_imc = nome

        # Altura
        if altura > maior_altura:
            maior_altura = altura
            nome_maior_altura = nome

        if altura < menor_altura:
            menor_altura = altura
            nome_menor_altura = nome

        # Peso
        if peso > maior_peso:
            maior_peso = peso
            nome_maior_peso = nome

        if peso < menor_peso:
            menor_peso = peso
            nome_menor_peso = nome

        # Nome mais curto e mais longo
        if nome_mais_longo == "" or len(nome) > len(nome_mais_longo):
            nome_mais_longo = nome
            
        if nome_mais_curto == "" or len(nome) < len(nome_mais_curto):
            nome_mais_curto = nome

        # Médias
        peso_med += peso
        alt_med += altura

    total = len(dados)
    peso_med /= total
    alt_med /= total

    print(f"Maior altura: {maior_altura:.2f} m ({nome_maior_altura})")
    print(f"Menor altura: {menor_altura:.2f} m ({nome_menor_altura})")

    print(f"Maior peso: {maior_peso:.2f} kg ({nome_maior_peso})")
    print(f"Menor peso: {menor_peso:.2f} kg ({nome_menor_peso})")

    print(f"Maior IMC: {maior_imc:.2f} ({nome_maior_imc})")
    print(f"Menor IMC: {menor_imc:.2f} ({nome_menor_imc})")

    print(f"Nome mais longo: {nome_mais_longo} ({len(nome_mais_longo)} caracteres)")
    print(f"Nome mais curto: {nome_mais_curto} ({len(nome_mais_curto)} caracteres)")

    print(f"Média do peso: {peso_med:.2f} kg")
    print(f"Média da altura: {alt_med:.2f} m")

    input("\nPressione Enter para voltar ao menu...")

def ler(dados):


    while True:
        limpa()
        print("MENU:")
        print("0 - SAIR")
        print("1 - LISTAR")
        print("2 - CONSULTAR")
        print("3 - CADASTRAR")
        print("4 - DELETAR")
        print("5 - ALTERAR")
        print("6 - IMC")
        print("7 - ESTATISTICAS")
        try:
            opc = int(input())

            if(opc == 0):
                limpa()
                return

            elif(opc == 1):
                limpa()

                if(len(dados) == 0):
                    input("Dataset vazio, aperte enter para voltar ao menu...")
                    continue

                lista(dados)
            
            elif(opc == 2):
                limpa()

                if(len(dados) == 0):
                    input("Dataset vazio, aperte enter para voltar ao menu...")
                    continue
                
                consultar(dados)

            elif(opc == 3):
                limpa()

                cadastrar(dados)

            elif(opc == 4):
                limpa()

                if(len(dados) == 0):
                    input("Dataset vazio, aperte enter para voltar ao menu...")
                    continue

                deletar(dados)

            elif(opc == 5):
                limpa()

                if(len(dados) == 0):
                    input("Dataset vazio, aperte enter para voltar ao menu...")
                    continue

                alterar(dados)
            
            elif(opc == 6):
                limpa()

                if(len(dados) == 0):
                    input("Dataset vazio, aperte enter para voltar ao menu...")
                    continue

                imc(dados)

            elif(opc == 7):
                limpa()

                if(len(dados) == 0):
                    input("Dataset vazio, aperte enter para voltar ao menu...")
                    continue

                estatisticas(dados)

        except:
            input("Caractere digitado não numerico")

def main():

    limpa()
    input("\nBEM-VINDO AO SISTEMA TABAJARA - BIOMETRICO\n\tAperte enter para ir ao menu...")

           
    ler(base())

    print("OBRIGADO POR ACESSAR O SISTEMA TABAJARA")

main() 
