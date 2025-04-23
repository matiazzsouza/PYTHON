def main():


    let = input("digite varias palavras:")

    lets = list(let)

    tam = len(let)

    esp = 0

    i = 0
    j = 0

    while(i < tam):
        
        if(lets[i] == ' '):
            esp += 1
    

        i += 1

    esp += 1
    mat = [[] for i in range(esp)]  # mateus souza marinho 2 espaços entao sao tres palavras
                                    # pensei em fazer uma matriz com i palavras e j letras 
                                    
    i = 0
    cont = 0

    while (i != esp):
        cont += 1
        while(j != ' '):
            mat[j] = lets[i]
            j +=1
        i += 1

    while(i < esp):
        print(f"{i + 1} palavra = {mat[i]}")
        i += 1
    



main()