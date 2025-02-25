n = int(input("Quantos alunos vão dar sua satisfação:"))
med = int

med = 0

vet: [int] = [0 for x in range(n)]

for i in range(0, n):
    vet[i] = int(input(f"\ndigite a nota do aluno {i + 1} -> "))
  
for i in range(0, n):
    med = med + vet[i]

med = med / n

print(f"\no valor da media aritmeticas é de -> {med}")    