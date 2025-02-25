salario = float(input("\ndigite o seu salario por hora:"))
horas = float(input("\nagora digite quantas horas voce trabalha por mês:"))

salario_total = salario * horas

salario_liquido = salario_total - (salario_total * 0.05 + salario_total * 0.1)

print(f"o valor do seu salario liquido é de = {salario_liquido} ")