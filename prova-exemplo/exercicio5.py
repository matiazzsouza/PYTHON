import os

def limpar_tela():
    # Para Windows
    if os.name == 'nt':
        os.system('cls')
        
def idade(age, custo):

    desc1 = 0

    if( 0 <= age <= 5 ):
        desc1 = 0.2
    
    if( 6 <= age <= 10 ):
        desc1 = 0.15
    
    if( 11 <= age <= 16 ):
        desc1 = 0.1
    
    if( 17 <= age <= 59 ):
        desc1 = 0
    
    if(  age >= 60 ):
        desc1 = 0.3

    total = custo * desc1

    return desc1, total #retorna o valor de desconto com o valor ja descontado

def bilhete(bi, custo):

    desc = 0

    if(bi == 1):
        desc = 0

    if(2 <= bi <=5):
        desc = 0.05
        
    if(6 <= bi <= 10):
        desc = 0.15

    if(bi >= 11):
        desc = 0.3

    total = custo * desc
        
    return desc, total #retorna o valor do desconto e qual o valor que sera descontado

def planos(custo):

    esc = int(input("\nDESEJA MELHORAR A SUA PASSAGEM OU CONTINUAR COM O BASICO(será acrescentado um valor final)?\n1-SIM\n2-NÃO, PREFIRO CONTINUAR COM O BASICO"))
    print("\n")
    if(esc != 1):
        return 0, 0

    else:
        esc2 = int(input("Nossos planos:\n1-Planetario(Passagem + 30%)\n2-Estelar(Passagem + 60%)\n3-Galatico(Passagem + 100%)\n4-Desistir"))
        if(esc2 == 1):
            valor = custo * 0.3 
            return 1, valor

        elif(esc2 == 2):
            valor = custo * 0.6
            return 2, valor
        
        elif(esc2 == 3):
            valor = custo * 2
            return 3, valor
        
        else:
            return 0, 0

def main():

    print("\n")
    print("*" * 70)
    print("\t*", "BEM VINDO AO SISTEMA DE ONIBUS DE RAPIDOPOLIS", "*")
    print("*"*70)
    print("\n")


    plano = ["Basico", "Planetario", "Estelar", "Galatico"]
    age = int(input("Qual a sua idade:"))
    bi = int(input("Quantos bilhetes foram adquiridos:"))
    distancia = int(input("Qual a distancia percorrida(Km):"))
    preco = 1.5 #preco por km percorrido 
    i = 0
    valor = 0
    

    custo = distancia  * preco

    i, valor = planos(custo)

    total = custo + valor # soma o valor total da corrida com o plano escolhido por ele e o desconto sera aplicado no valor total mesmo escolhendo o basico

    desc_ida, total_ida = idade(age, total)
    
    desc_bi, total_bi = bilhete(bi, total)



    total_desc = total_ida + total_bi #soma dos valor que seram descontados  
    
    totalmente = total - total_desc    #conta final para saber o valor final da corrida descontadno o valor de idade junto com o de bilhetes

    limpar_tela()

    print("\n")
    print("VALORES DA CORRIDA:")
    print("-"*60)
    print(f"VALOR INICIAL DA CORRIDA:{custo:.2f}")
    print(f"PLANO ESCOLHIDO: {plano[i]}")

    if(i != 0):
        print(f"VALOR DO PLANO: {valor}")
        print(f"VALOR COM O PLANO : {total}")

    print(f"DESCONTO PELA IDADE DE {age} ANOS: {total_ida}({desc_ida * 100:.0f}%)")
    print(f"DESCONTO PELA QUANTIDADE DE {bi} BILHETES: {total_bi:.2f}({desc_bi * 100:.0f}%)")
    print(f"VALOR A SER DESCONTADO: {total_desc}")
    print(f"VALOR FINAL DA CORRIDA: {totalmente:.2f}")
    print("-"*60)

main()
## Olá, sou Mateus Marinho, estudante de Engenharia de Software 💻✏

<div>
  <a href="https://beacons.ai/matiazzsouza">
  <img height="180em" src="https://github-readme-stats.vercel.app/api?username=matiazzsouza&show_icons=true&theme=synthwave&include_all_commits=true&count_private=true"/>
  <img height="180em" src="https://github-readme-stats.vercel.app/api/top-langs/?username=matiazzsouza&layout=compact&langs_count=16&theme=synthwave"/>
</div>
  
<div style="display: inline_block"><br>
  <img align="center" alt="Mateus-C" height="30" width="40" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/c/c-original.svg">
  <img align="center" alt="Mateus-C++" height="30" width="40" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/cplusplus/cplusplus-original.svg">
  <img align="center" alt="Mateus-HTML" height="30" width="40" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/html5/html5-original.svg">
  <img align="center" alt="Mateus-CSS" height="30" width="40" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/css3/css3-original.svg">
  <img align="center" alt="Mateus-JavaScript" height="30" width="40" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/javascript/javascript-plain.svg">
  <img align="center" alt="Mateus-Python" height="30" width="40" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg">
  <img align="center" alt="Mateus-Git" height="30" width="40" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/git/git-original.svg">
  <img align="center" alt="Mateus-GitHub" height="30" width="40" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/github/github-original.svg">
  <img align="center" alt="Mateus-Node" height="30" width="40" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/nodejs/nodejs-original.svg">
  <img align="center" alt="ROS2" height="40" width="40" src="https://upload.wikimedia.org/wikipedia/commons/b/bb/Ros_logo.svg">
  <img align="center" alt="Assembly" height="40" width="40" src="https://upload.wikimedia.org/wikipedia/commons/9/94/Microprocessor.svg">
  <img align="center" alt="MySQL" height="40" width="40" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/mysql/mysql-original.svg">
  <img align="right" alt="Mateus-gif" src="https://cdn.discordapp.com/attachments/795358919417397249/825430589581688872/hi.gif">
</div>
  
##
  
<div>
  <a href="https://mateusmarinho.github.io/" target="_blank">
    <img src="https://img.shields.io/badge/website-000000?style=for-the-badge&logo=About.me&logoColor=white" target="_blank">
  </a>
  
  <a href="mailto:mate4338@gmail.com">
    <img src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white" target="_blank">
  </a>
  
  <a href="https://instagram.com/matiazzsouza" target="_blank">
    <img src="https://img.shields.io/badge/-Instagram-%23E4405F?style=for-the-badge&logo=instagram&logoColor=white" target="_blank">
  </a>
  
  <a href="https://discord.com/users/SEU_ID" target="_blank">
    <img src="https://img.shields.io/badge/Discord-7289DA?style=for-the-badge&logo=discord&logoColor=white" target="_blank">
  </a> 
  
  <a href="https://www.linkedin.com/in/matiazzsouza" target="_blank">
    <img src="https://img.shields.io/badge/-LinkedIn-%230077B5?style=for-the-badge&logo=linkedin&logoColor=white" target="_blank">
  </a>
</div>
