
def main():

    pala = input("Digite o nome que deseja:")

    let = list(pala)

    tam = len(pala)


    i = 0 

    while(i < tam):

        if(let[i] == 'a' or let[i] == 'e' or let[i] == 'i' or let[i] == 'o' or let[i] == 'u' ):
            
            if(let[i] == "a" ):
                let[i] = '$'

            else:
                let[i] = "#"

        i += 1

    i = 0

    while(i < tam):

        temp = let[i]
        let[i] = let[tam - 1 - i]
        let[i] = temp

        print(f"{let[i]}")

        i += 1
        




main()