import numpy as np

def T(dia):
    
    return 10 + np.cos(dia / 3) * 5  

def main():
    dia = 0
    menor_temp = T(dia)
    dia_min = dia

    while (dia <= 30):
        
        temp_atual = T(dia)

        if (temp_atual < menor_temp):
            menor_temp = temp_atual
            dia_min = dia

        dia += 1

    print(f"O dia com a menor temperatura prevista é o dia {dia_min}, com temperatura de {menor_temp:.2f}°C.")


main()
