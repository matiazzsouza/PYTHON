import os

def limpa():
        os.system('cls')


def inserir(dados):

        limpa()
        print("Insira as informações do usuario:\n")
        try:
                nome = input("Digite o nome do usuario:")
                nome = nome.lower()
                idade = input("Digite a idade do usuario:")
                cpf = input("Digite o CPF do usuario:")
                tel = input("Digite o número de telefone do usuario:")

        except:
                print("Erro digite apenas numeros")

        dados[nome] = {
                "CPF": cpf,
                "Idade":idade,
                "Telefone": tel
        }



def consultar(dados):

        limpa()
        cpf = input("Digite o cpf do seu usuario:")

        for i in dados:
                if(dados[i]["CPF"] == cpf):
                        print(i)
                        print(dados[i])
                        input()

        
        return



def base():

        return {}




def ler(dados):

        limpa()
        print('BEM-VINDO AO SITE DE DADOS\n\tAPERTE ENTER PARA CONTINUAR...')
        input()

        while(True):        
                limpa()
                print("MENU:")
                print("1-Ver dados\n2-Inserir dados\n3-Consultar dados\n4-Deletar dados\n5-Sair")
                opc = int(input())
                if(opc > 5 or opc < 1):
                        limpa()
                        input("Opção invalkida digite novamente")
                if(opc == 1):
                        if(len(dados) == 0):
                                limpa()
                                input("Banco de dados vazia, aperte enter para voltar ao menu...")
                                continue
                        print(dados)
                        input("aperte enter para voltar ao menu...")
                
                elif(opc == 2):
                        inserir(dados)
                
                elif(opc == 3):
                        if(len(dados) == 0):
                                limpa()
                                input("Banco de dados vazia, aperte enter para voltar ao menu...")
                                continue
                        consultar(dados)
                
                elif(opc == 4):
                        if(len(dados) == 0):
                                limpa()
                                input("Banco de dados vazia, aperte enter para voltar ao menu...")
                                continue
                        deletar(dados)


                elif(opc == 5):
                        return



dados = base()  

ler(dados)

limpa()
print("Obrigado por acessar o nosso site")