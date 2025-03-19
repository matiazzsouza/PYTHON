

def verifica(cod):

    soma = 0
    i = 0

    for i in range(6):
        soma += cod[i]
    
    soma = soma % 10

    if(soma == cod[6]):
        return 1

    else:
        return 0


def main():

    cod = [0] * 7

    print("digite o seu codigo numero por numero:")

    for i in range(7):
        while(True):
            try:
                cod[i] = int(input(f"{i + 1}°:"))
                break
            except ValueError:
                print("caractere inserido não é um numero")
    
    num = verifica(cod)

    if(num == 1):
        print("verificação aceita")
    else:
        print("PEGA LADRAO")


main()