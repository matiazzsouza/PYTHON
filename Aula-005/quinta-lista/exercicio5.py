def main():

    i = 0
    cont = 0


    while(True):
        try:
            email = input("digite seu email")
            lista = list(email)
            break

        except:
            print("digite um email existente")

    tam = len(lista)


    while (i < tam):

        if(lista[i] != '@'):
            cont = 1
            i += 1
        else: 
            print("é um email")
            i = tam

        if(cont == 1):
            print("nao é um email")
            i = tam
    
    
    


main()