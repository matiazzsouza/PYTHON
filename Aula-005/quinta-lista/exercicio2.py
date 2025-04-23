
def main():

    ph = [7 ,6 ,7.5 ,7 ,6.8 ,7.1 ,6.9 ,6.4 ,6.5 ,6.7]

    i = 0
    maior = 0
    menor =  9999
    soma = 0
    jm = 0
    jme = 0


    while(i < len(ph)):
        soma += ph[i]

        if(ph[i] > maior):
            maior = ph[i]
    
        if(ph[i] < menor):
            menor = ph[i]

        i += 1


    soma /= i

    i = 0 

    while(i < len(ph)):

        if(ph[i] > soma):
            jm += 1
        else:
            jme += 1

        i += 1
    
    print(f"o maior valor é:{maior}")
    print(f"o menor valor é:{menor}")
    print(f"a media do valor é:{soma:.2f}")
    print(f"a quantidade de valores maior que a media é:{jm}")
    print(f"a quantidade de valores menor que a media é:{jme}")




main()  