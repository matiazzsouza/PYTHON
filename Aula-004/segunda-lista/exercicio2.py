def calcular_lucro(valor_produto):

    if valor_produto < 25:
        return 100
    elif valor_produto < 100:
        return 70
    elif valor_produto < 500:
        return 60
    elif valor_produto < 1000:
        return 50
    else:
        return 40

def main():
    
    valor_produto = float(input("Digite o valor do produto (R$): "))
    
    if valor_produto >= 0:
        
        lucro = calcular_lucro(valor_produto)
        print(f"O percentual mínimo de lucro para este produto é de {lucro}%.")
    else:
        print("Erro: O valor do produto não pode ser negativo.")


main()
