def descontos(iptu, age):
    
    val = 0
    desc = 0

    if age >= 5 and age < 20:
        
        val = iptu * 0.15
        desc =  iptu - val
    
    elif age >= 20 and age < 40:
        
        val = iptu * 0.25
        desc =  iptu - val

    elif age >= 40:
        
        val = iptu * 0.30
        desc =  iptu - val
    
    else:
        print("Não há desconto para este imóvel")


    return val, desc 

def main():

    print("\n")
    iptu = float(input("Digite o valor do iptu:"))
    age = int(input("Digite a idade do imovel:"))

    val, desc = descontos(iptu, age)

    print("-"*50)
    print(f"Valor do iptu sem desconto: {iptu}")
    print(f"Valor a ser descontado {val}")
    print(f"O valor do iptu com desconto é: {desc}")
    print("-"*50)

main()