peso = float
cm = float



peixes: [[float]] = [[0.0 for x in range(2)]for x in range(7)]

for i in range(7):
        peixes[i][0] = float(input("\ndigite o peso do peixe em kg:"))
        for j in range(1):
                peixes[i][j]= float(input("digite o comprimento do peixe em cm:"))
            
for i in range(7):
    print(f"\n\nPeixe {i + 1}")
    print(f"Peso (kg): {peixes[i][0]}")
    print(f"Tamanho (cm): {peixes[i][1]}")
