

def main():

    aux = 0

    n1 = int(input("Digite o primeiro número: "))
    n2 = int(input("Digite o segundo número: "))   
    n3 = int(input("Digite o terceiro número: "))

    if n1 > n2 :
        n1, n2 = n2, n1

    if n2 > n3:
        n2, n3 = n3, n2    
    
    if n1 > n2:
            n1, n2 = n2, n1
            

    print(f"Ordem crescente: {n1}, {n2}, {n3}")
        
        
    
    



main()