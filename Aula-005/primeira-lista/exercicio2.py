def main():

# O EXERCICIO 2 E 3 ESTAO JUNTOS 

    num = int(input("digite a quantidade de numeros para a media "))

    i = 0
    soma = 0
    maior = 0
    menor = 9999

    print("\n")
    while(i < num):

        num2 = int(input("digite um numero:"))
        
        if(num2 < menor):
            menor = num2
        
        if(num2 > maior):
            maior = num2

        soma += num2

        i+=1

    soma /= i

    print("\n")
    print("-"*50)
    print(f"o valor da media desses numeros é de: {soma}")
    print(f"o maior valor digitado é de: {maior}")
    print(f"o menor valor digitado é de: {menor}")
    print("-"*50)
    print("\n")


main()