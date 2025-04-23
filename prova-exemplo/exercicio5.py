import os

def limpar_tela():
    # Para Windows
    if os.name == 'nt':
        os.system('cls')
        
def idade(age, custo):

    desc1 = 0

    if( 0 <= age <= 5 ):
        desc1 = 0.2
    
    if( 6 <= age <= 10 ):
        desc1 = 0.15
    
    if( 11 <= age <= 16 ):
        desc1 = 0.1
    
    if( 17 <= age <= 59 ):
        desc1 = 0
    
    if(  age >= 60 ):
        desc1 = 0.3

    total = custo * desc1

    return desc1, total #retorna o valor de desconto com o valor ja descontado

def bilhete(bi, custo):

    desc = 0

    if(bi == 1):
        desc = 0

    if(2 <= bi <=5):
        desc = 0.05
        
    if(6 <= bi <= 10):
        desc = 0.15

    if(bi >= 11):
        desc = 0.3

    total = custo * desc
        
    return desc, total #retorna o valor do desconto e qual o valor que sera descontado

def planos(custo):

    esc = int(input("\nDESEJA MELHORAR A SUA PASSAGEM OU CONTINUAR COM O BASICO(será acrescentado um valor final)?\n1-SIM\n2-NÃO, PREFIRO CONTINUAR COM O BASICO"))
    print("\n")
    if(esc != 1):
        return 0, 0

    else:
        esc2 = int(input("Nossos planos:\n1-Planetario(Passagem + 30%)\n2-Estelar(Passagem + 60%)\n3-Galatico(Passagem + 100%)\n4-Desistir"))
        if(esc2 == 1):
            valor = custo * 0.3 
            return 1, valor

        elif(esc2 == 2):
            valor = custo * 0.6
            return 2, valor
        
        elif(esc2 == 3):
            valor = custo * 2
            return 3, valor
        
        else:
            return 0, 0

def main():

    print("\n")
    print("*" * 70)
    print("\t*", "BEM VINDO AO SISTEMA DE ONIBUS DE RAPIDOPOLIS", "*")
    print("*"*70)
    print("\n")


    plano = ["Basico", "Planetario", "Estelar", "Galatico"]
    age = int(input("Qual a sua idade:"))
    bi = int(input("Quantos bilhetes foram adquiridos:"))
    distancia = int(input("Qual a distancia percorrida(Km):"))
    preco = 1.5 #preco por km percorrido 
    i = 0
    valor = 0
    

    custo = distancia  * preco

    i, valor = planos(custo)

    total = custo + valor # soma o valor total da corrida com o plano escolhido por ele e o desconto sera aplicado no valor total mesmo escolhendo o basico

    desc_ida, total_ida = idade(age, total)
    
    desc_bi, total_bi = bilhete(bi, total)



    total_desc = total_ida + total_bi #soma dos valor que seram descontados  
    
    totalmente = total - total_desc    #conta final para saber o valor final da corrida descontadno o valor de idade junto com o de bilhetes

    limpar_tela()

    print("\n")
    print("VALORES DA CORRIDA:")
    print("-"*60)
    print(f"VALOR INICIAL DA CORRIDA:{custo:.2f}")
    print(f"PLANO ESCOLHIDO: {plano[i]}")

    if(i != 0):
        print(f"VALOR DO PLANO: {valor}")
        print(f"VALOR COM O PLANO : {total}")

    print(f"DESCONTO PELA IDADE DE {age} ANOS: {total_ida}({desc_ida * 100:.0f}%)")
    print(f"DESCONTO PELA QUANTIDADE DE {bi} BILHETES: {total_bi:.2f}({desc_bi * 100:.0f}%)")
    print(f"VALOR A SER DESCONTADO: {total_desc}")
    print(f"VALOR FINAL DA CORRIDA: {totalmente:.2f}")
    print("-"*60)

main()

