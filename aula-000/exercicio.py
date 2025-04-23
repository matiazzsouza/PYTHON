import mysql.connector
from mysql.connector import Error

def conectar():
    try:
        conexao = mysql.connector.connect(
            host="localhost",
            port=3306,
            user="root",
            password="Ma070905!",
            database="aula_python"
        )
        return conexao
    except Error as erro:
        print(f"❌ Erro ao conectar: {erro}")
        return None

def criar_tabela():
    conexao = conectar()
    if conexao:
        cursor = conexao.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS pessoas (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(100),
            idade INT
        )
        """)
        conexao.commit()
        cursor.close()
        conexao.close()


def inserir_pessoa():
    nome = input("📝 Digite o nome: ")
    idade = int(input("🎂 Digite a idade: "))

    conexao = conectar()
    if conexao:
        try:
            cursor = conexao.cursor()
            sql = "INSERT INTO pessoas (nome, idade) VALUES (%s, %s)"
            dados = (nome, idade)
            cursor.execute(sql, dados)
            conexao.commit()
            print("✅ Pessoa inserida com sucesso!")
        except Error as erro:
            print(f"❌ Erro ao inserir: {erro}")
        finally:
            cursor.close()
            conexao.close()

def listar_pessoas():
    conexao = conectar()
    if conexao:
        try:
            cursor = conexao.cursor()
            cursor.execute("SELECT * FROM pessoas")
            resultados = cursor.fetchall()

            if resultados:
                print("\n📋 Pessoas cadastradas:")
                for linha in resultados:
                    print(f"🆔 ID: {linha[0]} | 🧑 Nome: {linha[1]} | 🎂 Idade: {linha[2]}")
            else:
                print("⚠️ Nenhuma pessoa cadastrada.")
        except Error as erro:
            print(f"❌ Erro ao listar: {erro}")
        finally:
            cursor.close()
            conexao.close()

def menu():
    criar_tabela() 
    while True:
        print("\n📚 MENU")
        print("1 - Inserir nova pessoa")
        print("2 - Listar pessoas")
        print("3 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            inserir_pessoa()
        elif opcao == "2":
            listar_pessoas()
        elif opcao == "3":
            print("👋 Saindo...")
            break
        else:
            print("❌ Opção inválida!")

menu()
