def veri(a, l):

    if (20 <= l <= 25 and 25 <= a <= 30):
        return 1
    elif (26 <= l <= 30 and 31 <= a <= 35):
        return 2
    elif (31 <= l <= 35 and 36 <= a <= 40):
        return 3
    elif (36 <= l <= 40 and 41 <= a <= 45):
        return 4
    elif (41 <= l <= 45 and 46 <= a <= 50):
        return 5
    elif (46 <= l <= 50 and 51 <= a <= 55):
        return 6
    elif (51 <= l <= 55 and 56 <= a <= 60):
        return 7
    else:
        return -1 

def main():

    a = int(input("Digite a altura da camisa(cm): "))
    l = int(input("Digite a largura da camisa(cm): "))

    num = veri(a, l)

    if (num == 1):
        print("O seu tamanho é P")
    elif (num == 2):
        print("O seu tamanho é M")
    elif (num == 3):
        print("O seu tamanho é G")
    elif (num == 4):
        print("O seu tamanho é XG")
    elif (num == 5):
        print("O seu tamanho é XXG")
    elif (num == 6):
        print("O seu tamanho é 3X")
    elif (num == 7):
        print("O seu tamanho é 4X")
    else:
        print("Tamanho inexistente na loja")

main()
