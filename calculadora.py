
def soma():
    
    num:float = 0
    i: int = 1
    num2:float = 0
    print("\n\n\t\tDigite o numero -1 para parar a soma")
    
    num = float(input(f"\nNumero {i}-> "))  
    
    while(num2 != -1):
        i += 1
        num2 = float(input(f"\nNumero {i}-> "))
        num += num2

        res = num
        
        if(num2 != -1):
            print(f"\nresultado: {res}")

    print(f"\nresultado final: {res + 1}")
        

    return

def sub():
        
    num:float = 0

    i: int = 1
    num2:float = 0
    print("\n\n\t\tDigite o numero -1 para parar a subtração")
    
    num = float(input(f"\nNumero {i}-> "))  
    
    while(num2 != -1):
        i += 1
        num2 = float(input(f"\nNumero {i}-> "))
        num -= num2
        res = num
        if(num2 != -1):
            print(f"\nresultado: {res}")
        
    print(f"\nresultado: {res - 1}")
        

    return

def mul():
    
    num:float = 1
    i: int = 1
    num2:float = 1
    print("\n\n\t\tDigite o numero -1 para parar a multiplicação")
    
    num = float(input(f"\nNumero {i}-> "))  
    
    while(num2 != -1):
        i += 1
        num2 = float(input(f"\nNumero {i}-> "))
        num *= num2
        res = num
        if(num2 != -1):
            print(f"\nresultado: {res}")

    print(f"\nresultado: {res * - 1}")
        
    
    return

def div():
    
    num:float = 0
    i: int = 1
    num2:float = 0
    print("\n\n\t\tDigite o numero -1 para parar a divisão")
    
    num = float(input(f"\nNumero {i}-> "))  
    
    while(num2 != -1):
        i += 1
        num2 = float(input(f"\nNumero {i}-> "))
        num /= num2
        res = num
        if(num2 != -1):
            print(f"\nresultado: {res:.2f}")
        

    print(f"\nresultado: {res * -1:.2f}")
        

        

    return

def porc():
    
    num:float = 0
    num2:float = 0
    
    
    num = float(input("\nDigite um numero:"))
    num2 = int(input("\nDigite o valor da porcentagem:"))
    
    por = num2
    
    num2 /= 100
    
    res = num * num2 
    
    print(f"\nNumero digitado = {num}")
    print(f"Porcentagem = {por}%")
    print(f"Resultado = {res}")

    return

def pot():
    
    num:float = 0
    num2:int = 0
    
    
    num = float(input("\nDigite o valor da base:"))
    num2 = int(input("\nDigite o valor do expoente:"))
        
    res = num ** num2
    
    print(f"\nNumero da base = {num}")
    print(f"Numero do expoente= {num2}")
    print(f"Resultado = {res}")

    return
        
def ler():

    print("\n\n\t\tOLA SEJA BEM-VINDO A CALCULADRA DO MATIAZ\n\t\t\t\tAPERTE ENTER PARA COMEÇAR")
    input()
    
    test: int
    print("\n1-)SOMA\n2-)SUBTRÇÃO\n3-)MULTIPLICAÇÃO\n4-)DIVISÃO\n5-)PORCENTAGEM\n6-)POTÊNCIAÇÃO\n7-)SAIR")
    num = int(input("AGORA DIGITE A OPERAÇÃO QUE VOCE DESEJA:"))
    
    
    if(num == 1):
        soma()
        test = int(input("\n\nDeseja continuar na calculadora?\n1)-Sim\n2-)Não\n"))
        if(test != 1):
            return
        else:
            ler()
            
    elif(num == 2):
        sub()
        test = int(input("\n\nDeseja continuar na calculadora?\n1)-Sim\n2-)Não\n"))
        if(test != 1):
            return
        else:
            ler()
            
    elif(num == 3):
        mul()
        test = int(input("\n\nDeseja continuar na calculadora?\n1)-Sim\n2-)Não\n"))
        if(test != 1):
            return
        else:
            ler()
            
    elif(num == 4):
        div()
        test = int(input("\n\nDeseja continuar na calculadora?\n1)-Sim\n2-)Não\n"))
        if(test != 1):
            return
        else:
            ler()
            
    elif(num ==5):
        porc()
        test = int(input("\n\nDeseja continuar na calculadora?\n1)-Sim\n2-)Não\n"))
        if(test != 1):
            return
        else:
            ler()
            
    elif(num == 6):
        pot()
        test = int(input("\n\nDeseja continuar na calculadora?\n1)-Sim\n2-)Não\n"))
        if(test != 1):
            return
        else:
            ler()
            
    elif(num == 7):
        return
     
    else:
        print("\nOPERAÇÃO NÃO ENCONTRADA DIGITE NOVAMENTE")
        ler()
    
    return

def main():
    
  
    
    ler()
    
    print("\n\n\t\tOBRIGADO POR ACESSAR A CALCULADORA\n\t\t\t\t\tVOLTE SEMPRE")
    
main()

