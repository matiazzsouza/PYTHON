def main():
    
    #EXERCICIO 9 COM A 10

    qnt = int(input("Quantas linhas você deseja: "))

    aster = "*"

    for i in range(qnt):
        print(aster)
        aster += "*"


    print("\n")

    for i in range(qnt):
        espacos = " " * (qnt - i - 1)       
        ast = "*" * (2 * i + 1)             
        print(espacos + ast)

main()
