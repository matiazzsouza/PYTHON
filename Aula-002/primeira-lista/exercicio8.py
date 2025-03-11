

def main():

peixes: [[float]] = [[0.0 for x in range(2)] for x in range(7)]

for i in range(7):
    peixes[i][0] = float(input(f"\nDigite o peso do peixe {i + 1} em kg: "))
    peixes[i][1] = float(input(f"Digite o comprimento do peixe {i + 1} em cm: "))

for i in range(7):
    print(f"\nPeixe {i + 1}")
    print(f"Peso (kg): {peixes[i][0]}")
    print(f"Comprimento (cm): {peixes[i][1]}")

soma_mc = sum(peixes[i][0] * peixes[i][1] for i in range(7))
soma_c = sum(peixes[i][1] for i in range(7))

if soma_c == 0:
    print("\nErro: A soma dos comprimentos não pode ser zero.")
else:
    media_ponderada = soma_mc / soma_c
    print(f"\nA média ponderada da massa dos peixes é: {media_ponderada:.2f} kg")


main()