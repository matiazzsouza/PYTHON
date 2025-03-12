
def tabuada(num):

    i = 0
    res = 0

    print(f"TABUADA DO {num}\n")

    while(i <= 10):
        res = num * i
        print(f"{num} X {i} = {res}")
        i+=1
    print("\n")
    
    return

def main():

    print("-"*50)
    print("\t\tSEJA BEM-VINDO A TABUADA")
    print("-"*50)
    print("\n")

    num = int(input("DIGITE UM NUMERO:"))  
    print("\n")

    tabuada(num)

main()