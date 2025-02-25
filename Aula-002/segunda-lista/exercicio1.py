#banco de rapidopolis



def dolar():
    
    dolar = 5.77
    
    qd = float(input("\nDigite a quantidade de dólares que deseja:"))

    total = qd * dolar + 10
    
    total = total + total * 0.02
    total = total + total * 0.06
    
    return total 
    

def euro():
    
    euro = 6.2
    
    qe = float(input("\nDigite a quantidade de euros que deseja:"))

    total = qe * euro + 10
    
    total = total + total * 0.02
    total = total + total * 0.06
    
    return total


def libra():
    
    libra = 7.235
    
    ql = float(input("\nDigite a quantidade de libras que deseja:"))
    
    total = ql * libra + 10
    
    total = total + total * 0.02
    total = total + total * 0.06
    
    return total

def peso():    
    peso = 0.54
    
    qp = float(input("\nDigite a quantidade de pesos que deseja:"))
    
    total = qp * peso + 10
    
    total = total + total * 0.02
    total = total + total * 0.06
    
    return total 

def main():
 
    print("\n\nOLA SEJA BEM-VINDO AO BAR – BANK ARTIFICIAL DE RAPIDÓPOLIS: ")
    
    input()
      
    print("ABAIXO ESTA O VALOR DAS MOEDAS ATUALIZADAS:\n1-)DOLAR:5,77\n2-)EURO:6,20\n3-)LIBRA:7,235\n4-)PESO(ARG):0,54")
    
    n = int(input("\nDigite o numero da moeda que deseja comprar?"))
    
    if(n == 1):
        res = dolar()
        print(f"o valor total a ser pago é de {res:.2f}")
    elif(n == 2):
        res = euro()
        print(f"o valor total a ser pago é de {res:.2f}")
    elif(n == 3):
        res = libra()
        print(f"o valor total a ser pago é de {res:.2f}")
    elif(n == 4):
       res = peso()
       print(f"o valor total a ser pago é de {res:.2f}")
    else:
        print("opção nao encontrada digite novamente")


main()
    
