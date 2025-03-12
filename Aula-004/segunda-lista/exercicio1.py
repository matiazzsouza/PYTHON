
def main():


    
    print("\n")
    print("-"*50)
    print("\t\tSITE DA PREFEITURA")
    print("-"*50)

    print("\n")
    idade = int(input("Digite a sua idade:"))

    print("\n")

    if(idade < 16):
        print("Eleitor não obrigatorio")

    elif(idade >= 18 and idade < 65):
        print("Eleitor obrigatorio!!")

    else:
        print("Eleitor facultativo")


main()