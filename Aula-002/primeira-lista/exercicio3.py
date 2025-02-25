ls = float(input("\ndigite a largura da sala:"))
cs = float(input("\ndigite o comprimento da sala:"))

lp = float(input("digite a largura do piso:"))
cp = float(input("digite o comprimento do piso:"))

qnt = (ls * cs) / (lp * cp)

print(f"A quantidade de azulejos que sera usado é de -> {qnt}")