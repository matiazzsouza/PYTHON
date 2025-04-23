
def main():

    temp = [10,12,9,8,9,9,10,11,12,14,12,11]

    i = 0
    maior = 0
    menor = 9999
    soma = 0

    while(i < len(temp)):
        soma += temp[i]
        
        if(temp[i] > maior):
            maior = temp[i]
        
        if(temp[i] < menor):
            menor = temp[i]

        i += 1

    print(f"A maior temperatura é: {maior}")    
    print(f"A maior temperatura é: {menor}")    
    print(f"A media das temperaturas é: {soma / i:.2f}")


main()