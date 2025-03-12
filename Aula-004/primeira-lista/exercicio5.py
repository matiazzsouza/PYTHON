# media ponderada primeira prova vale 0,4 e a segunda 0,6


def medias(n1, n2):
    
    media = (n1 * 0.4 ) + (n2 * 0.6)/ (0.4 + 0.6)
    
    return media


def main():

    n1 = float(input("\nDigite a nota da primeira prova: "))
    n2 = float(input("Digite a nota da segunda prova: "))

    media = medias(n1, n2)

    print("\n")
    if(media < 5):
        print(f"Reprovado com média: {media}")
        
    elif(media >= 8 and media < 9):
        print(f"PARABENS O DESEMPENHO FOI MTO BOM: {media}")
    
    elif(media >= 9):    
        print(f"PARABENS, VOCE FOI APROVADO COM LOUVOR: {media}")

    else:
        print(f"Aprovado com média: {media}")
        
        

main()