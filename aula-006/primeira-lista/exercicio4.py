def main():

    qnt = int(input("quantos numeros voce deseja "))

    vet = []

    for i in range(qnt):
        aux = int(input(f"digite o {i + 1}° numero"))
        vet.append(aux)

    vet.sort()


    print(vet)

main()