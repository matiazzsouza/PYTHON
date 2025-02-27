def main():

    n = int(input("Digite um número: "))

    n2 = int(input("Digite outro número: "))

    if n % n2 == 0:
        print(f'O número {n} é divisível por {n2}.')
    else:  
        print(f'O número {n} não é divisível por {n2}.')

main()