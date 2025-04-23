def main():

    letra = input("digite uma palavra:")

    pala = list(letra)

    i = 0 
    esp = 0
    espe = 0
    vog = 0
    cos = 0
    ls = 0
    sla = 0
    a = 0
    e = 0
    ic = 0
    o = 0
    u = 0

    l = input("qual letra voce deseja contar?")

    while(i < len(letra)):
        
        if(pala[i] != 'a' and  pala[i] != 'e' and pala[i] != 'i' and pala[i] != 'o' and pala[i] != 'u' ):
            
            if(pala[i] == l ):
                cos += 1
                ls += 1      

            elif(pala[i] == ' '):
                esp += 1

            elif(pala[i] == "“" or pala[i] == "."  or pala[i] == "#" or pala[i] == "$" or pala[i] == "%"  or pala[i] == "?" or pala[i] == "!"):
                espe += 1
            
            else:
                cos += 1

        else:
            vog += 1
            sla = pala[i]

            if(sla == "a"):
                a += 1
            
            elif(sla == "e"):
                e += 1
            
            elif(sla == "i"):
                ic += 1
            
            elif(sla == "o"):
                o += 1
            
            elif(sla == "u"):
                u += 1


        i += 1



    print(f"\n\nPALAVRA DIGITADA: {letra.upper()}")

    print("-"*50)
    print(f"quantidade de a:{a}")
    print(f"quantidade de e:{e}")
    print(f"quantidade de i:{ic}")
    print(f"quantidade de o:{o}")
    print(f"quantidade de u:{u}")
    print("-"*50)

    print(f"quantidade de vogais:{vog}")
    print(f"quantidade de consoantes:{cos}")
    print("-"*50)

    print(f"quantidade de espaços:{esp}")
    print(f"quantidade de especiais:{espe}")
    print(f"quantidade de letra {l}:{ls}")
    print("-"*50)


main()