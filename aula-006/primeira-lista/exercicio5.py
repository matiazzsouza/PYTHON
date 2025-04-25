def main():

    aux = 0

    qnt = int(input("Quantos números voce deseja digitar:"))

    vet = []

    for i in range(qnt):
        num = int(input(f"digite o {i +1}° numero:"))
        vet.append(num)

    for i in range(qnt ):
        for j in range(qnt - 1):
            if(vet[j] > vet[j + 1]):
                aux = vet[j + 1]
                vet[j + 1] = vet[j]
                vet[j] = aux

    print(vet)


main()