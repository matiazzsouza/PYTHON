
#EXERCICIO 11 E 12 JUNTOS


def main():

    print("-"*40)
    num = int(input("digite o primeiro numero:"))
    num2 = int(input("digite o segundo numero:"))
    vet = [i for i in range(num2)]
    num3 = int(input("numero para a divisibilidade:")) 
    i = 0
    print("-"*40)

    while(num < num2):
        if(num % num3 == 0):
            vet[i] = num
            i += 1
        num += 1

    print(f"a quantidade de numeros divisiveis por 3 nesse intervalo é de: {i}\n")        

    print("os numeros são: ", end = "")

    for i in range(i):
        print(f"{vet[i]}\t", end = "")

main()