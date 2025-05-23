def main():

    ponteiro = open("teste.txt", "r")

    aux = ponteiro.read()
    ponteiro.close()

    aux = aux.split()  # divide em uma lista com base nos espaços ou quebras de linha, sem o uso de argumentos ele ira retirar todos os valores em branco do arquivo
    
    #verifica se o index que eu estou usando é igaul um caractere ou um digito "nomedavariavel".isalpha() para letra e .isdigit() para numeros

    soma = 0
    j = 0
    for i in aux:
        if(i.isdigit()):
            i = int(i)
            soma += i
            j += 1

    print(soma/j)

main()
