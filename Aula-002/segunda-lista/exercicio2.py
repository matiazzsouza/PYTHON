    
def main():

    print("\nSEJA BEM-VINDO AO ChaCoB- CHÂteau COusin Botyn")
    
    preco = float(input("\nQual o valor da porção consumida:"))
    
    qnt = int(input("\nQuantas porções foram servidas a mesa:"))
             
    conta_inicial = preco * qnt
    conta = conta_inicial
    
    desconto = (conta * 0.02) * qnt
    
    conta -= desconto
    
    conta += 20
    
    conta2 = (0.1 * conta)
    
    conta += conta2
    
        
    print("\n" + "-" * 40)
    print(f"{'Valor inicial:':<30} R$ {conta_inicial:>7.2f}")
    print(f"{'Desconto por porção:':<30} R$ {desconto:>7.2f}")
    print(f"{'Valor do couvert artístico:':<30} R$ {20:>7.2f}")
    print(f"{'Valor da taxa de serviço:':<30} R$ {conta2:>7.2f}")
    print("-" * 40)
    print(f"{'Total da conta:':<30} R$ {conta:>7.2f}")
    print("-" * 40)    

main()
    

    