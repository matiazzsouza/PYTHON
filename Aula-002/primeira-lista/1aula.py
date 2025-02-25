
print("\t\t\tDADOS DA SALA:\n")
cs= int(input("\t\t\tDIGITE O COMPRIMENTO DA SALA:  "))
ls = int(input("\t\t\tdigite o comprimento da sala:  "))


print("\n\t\t\tDADOS DO PISO:\n")
cp = int(input("\t\t\tdigite o comprimento do piso:  "))
lp = int(input("\t\t\tdigite a largura do piso:  "))


area = cs * ls
area2=cp * lp
npisos=area/area2

print("\n\t\t\tRESULTADOS DAS CONTAS DA SALA: \n")

print("\t\t\tcomprimento da sala:  ", cs, "cm")
print("\t\t\tlargura da sala: ", ls, "cm")
print("\t\t\tcomprimento do piso:  ", cp, "cm")
print("\t\t\tlargura do piso:  ", lp, "cm")

print("\t\t\tarea da sala:  ", area, "cm²")

print("\t\t\tarea do piso:  ", area2, "cm²")

print("\t\t\tnumero de pisos:  ", npisos)