

def calculo(x):
    
    resultado = (4 * x**2 - 3 * x + 9) / x
    
    print(f"O resultado da expressão é: {resultado}")

    return

def main():


    x = float(input("digite o valor do x:"))

    if x == 0:
        print("Não é possível dividir por zero!")
    else:
        calculo(x)
    

main()