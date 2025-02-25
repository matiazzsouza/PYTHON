#salario burto

def main():
    
    sh = float(input("\nDigite o valor do seu salario hora:"))
    horas = int(input("\nDigite quantas horas voce trabalha por mês"))
        
    sb = sh * horas
    pir: int
    ir: int
    pit: int
        
    if(sb < 1000):
            pir = 0.1
    
    if (sb >= 0 and sb < 3000):
           pir = 0.15
         
    if(sb >= 3000):
            pir = 0.225
            
    

main()
            
        
        
            