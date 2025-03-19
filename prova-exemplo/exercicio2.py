# calcular a media das calorias ingeridas e a maior e menor caloria ingerida pelos usuarios =

def main():

    vet = [i for i in range(10)]
    i = 0
    j = 0
    maior = 0
    menor = 9999
    som = 0

    print("\nDigite a quantidade de calorias ingeridas:")

    while(i < 10):
        vet[i] = int(input(f"{i + 1}° participante:"))
        if(vet[i] > maior):
            maior = vet[i]

        if(vet[i] < menor):
            menor = vet[i]

        if(vet[i] > 2000):
            j += 1


        som += vet[i]
        i += 1

    som /= i

    print("-"*50)
    print("RESULTADOS FINAIS:")
    print(f"MEDIAS DAS CALORIAS:{som:.2f}")
    print(f"MAIOR CALORIA REGISTRADA:{maior}")
    print(f"MENOR CALORIA REGISTRADA:{menor}")
    print(f"USUARIOS QUE CONSOMEM MAIS QUE 2000 KCAL:{j}")

    print("-"*50)



main()