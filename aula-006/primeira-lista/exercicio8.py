

def consulta(nomes):


    nomeC = input("digite o nome que deseja consultar:")

    for i in nomes:
        if(i == nomeC):
            print("Esse nome ja esta cadastrado")
            return
    
    print("Nome nao cadatrado")

    opcao = int(input("\nDeseja consultar mais algum nome:\n1)Sim\n2)Não"))
    

    if(opcao == 1):
        consulta(nomes)

    return

def main():

    nomes = []


    qnt = int(input("quantos nomes deseja escrever:"))

    for i in range(qnt):
        nome = input(f"{i + 1}° nome:")
        nomes.append(nome)

    opcao = int(input("\nDeseja consultar mais algum nome:\n1)Sim\n2)Não"))


    if(opcao == 1):
        consulta(nomes)

    
    print("obrigado por ler esse lindo codigo")

main()