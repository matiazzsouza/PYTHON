def main():

    num = int(input("digite um numero:"))
    num2 = int(input("digite outro numero:"))

    print(f"numeros entre {num} e {num2}")

    while(num < num2):
        num+=1
        if(num != num2):
            print(f"\nnumeros: {num}")
        

main()