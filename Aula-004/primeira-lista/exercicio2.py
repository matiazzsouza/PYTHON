

def main():

    lado1 = float(input("Digite o primeiro lado do triângulo: "))   
    lado2 = float(input("Digite o segundo lado do triângulo: "))
    lado3 = float(input("Digite o terceiro lado do triângulo: "))

    if (lado1 == lado2 and lado2 == lado3):
        print("\nTriângulo Equilátero")
    elif (lado1 == lado2 or lado1 == lado3 or lado2 == lado3):
        print("\nTriângulo Isósceles")
    else:
        print("\nTriângulo Escaleno")
    
    return
    
main()