
def vetor_matriz(matriz,vetor, J,opc):

    vet = []
    soma = 0    
    somas = []

    if(opc == 1):
        for i in range(J):
            soma = 0
            for j in range(len(matriz)):
                soma = matriz[j][i] * vetor[j] + soma
                
            vet.append(soma)
            
        return vet

    for i in range(len(matriz)):
        somas = []
        for j in range(len(vetor)):
            soma = matriz[i][0] * vetor[j]

            somas.append(soma)

        vet.append(somas)

    return vet




def main():
    
    matriz = [
        [1],
        [4],
        [7]
    ]

    vet = [1,2,3]

    #vai formar uma matriz 1x3

    cont = 0   

    for i in matriz:
        for j in i:
            cont += 1
        break

    res = 0

    opc = 0

    if(cont == 1):#matriz x vetor
        res = vetor_matriz(matriz,vet, cont, opc)
        print(res)

    elif(len(vet) == len(matriz)):#vetor x matriz
        opc = 1
        res = vetor_matriz(matriz,vet, cont, opc)
        print(res)
        
    else:
        print("não é possivel fazer a conta as linhas e colunas sao incompativeis")





main()