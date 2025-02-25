

x = float

y = float

velo: [float] = [0 for x in range(3)]

dest: [float] = [0 for x in range(3)]

temp: [int] = [0 for x in range(3)]


    #loop para armazenar as informações da corrida 
for i in range(0, 3): 
    dest[i] = float(input(f"\ndigite a distancia percorrida na {i + 1} parte:"))
    temp[i] = int(input("agora o tempo percorrido nesse percurso em min:"))
    velo[i] = dest[i] / temp[i]
    
    
    #loop para somar as medias totais do percurso
for i in range(0, 3):
    x = velo[i]
    velos = x + velo[i + 1]
    
    
velo_max = velos / 4
    

for i in range(0, 3, 2):
    ace = (velo[i] + velo[i + 1]) / (temp[i] + temp[i + 1])
    
    
for i in range(0, 3):
    print(f"\nA velocidade media do {i + 1} percurso é de = {velo[i]}")


print(f"a velocidade media total é de: {velo_max}")
print(f"A aceleração é de: {ace}") 
    
    