def main():

    n = int(input("digite o numero para o fatorial:"))
    num = n

    while(n > 1):

        num = num * (n -1)

        print("\n")
        print(f"{n}")
        print(f"{num}")

        n -= 1
        
    print(f"\no valor do fatorial é de = {num}")



main()
