def bina(num):

    aux = 0
    bins = []

    if(num == 1):
        return 1
    
    while(num != 0):
        binas = num % 2 #pega o resto e coloca no vetor bin
        num = num // 2 #divide o valor do num inicial assim fazendo um loop que fica ate ser 1 ou 0

        print(num)

        bins.append(binas)

    j = len(bins) - 1

    novo = []

    while(j >= 0):
        aux = bins[j]

        novo.append(aux)

        j -=1
        
    return novo




def main():


    num = int(input("Digite um numero para transfomra-lo em bínario:"))

    res = bina(num)

    print(res)

main()