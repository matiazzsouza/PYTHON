def calculo_imc(peso, altura):

    imc = peso / (altura ** 2)

    print("\n")
    if imc >= 18.5 and imc < 24.9:
        print(f"IMC: {imc:.2f}")
        print("Peso normal")
        
    elif imc >= 25 and imc < 29.9:
        print(f"IMC: {imc:.2f}")
        print("Sobrepeso")
        
    elif imc > 30:
        print(f"IMC: {imc:.2f}")
        print("Obesidade")

    else:
        print(f"IMC: {imc:.2f}")
        print("Abaixo do peso")

    return 

def main():

    print("\n")
    print("-"*50)
    print("Bem vindo a calculadora de IMC")
    print("-"*50)
    print("\n")

    peso = float(input("Digite o seu peso(KG):"))
    altura = float(input("Digite a sua altura(metros):"))

    calculo_imc(peso, altura)





main()