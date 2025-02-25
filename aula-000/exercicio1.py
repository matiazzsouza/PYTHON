def main():
    print("\nSISTEMA DE SEGURANÇA PUC\n")
    
    #se eu quiseer um pin eu uso o int ou o float, senao uso apenas o input
    
    
    #exemplo: senha = int(input("cadastre uma senha:"))
    senha = input("cadastre uma senha:")
     
    seg = input("confirme a senha:")
             
    if(senha != seg):
        print("senha errada")
    else:
        print("senha cadastrada")

main()