def main():

    qnt = int(input("Quantos numeros voce deseja digitar:"))

    vet = [i for i in range(qnt)]

    soma = 0
    maior = 0 
    menor = 9999

    for i in range(0, qnt):
        vet[i] = int(input(f"{i + 1}° número:"))
        if(vet[i] < menor):
            menor = vet[i]

        if(vet[i] > maior):
            maior = vet[i]

        soma += vet[i]
    
    soma /= qnt

    print(maior)
    print(menor)
    print(soma)

main()