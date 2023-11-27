import pyodbc
import pandas as pd

def cadastrar_contato():
    id_contato = input("ID: ")
    nome = input("Nome: ")
    instagram = input("Instagram: ")
    email = input("Email: ")

    for id in id_contato:
        if(id == id_contato):
            
        else:
            comando = f"INSERT INTO contato(id_contato, nome, instagram, email) VALUES ({id_contato}, '{nome}', '{instagram}', '{email}')"

    cursor.execute(comando)
    cursor.commit()

print("registro gravado")

# ////////////////////////////////////////////////////

try:
    dados_conexao = (
        "Driver={SQL Server};"
        "Server=localhost;"
        "Database=PythonSQL;"
        "User='sa';"
        "Password=123456;"
    )

    conexao = pyodbc.connect(dados_conexao)
    print("Conexão Bem Sucedida")

    cursor = conexao.cursor()
    cursor_cadastro = conexao.cursor()
    cursor_consulta = conexao.cursor()
    cursor_alteracao = conexao.cursor()
    cursor_exclusao = conexao.cursor()

except:
    print("Ocorreu algum erro no BD")
else:
    print("Conexão Bem Sucedida")

print("""
      1 - Cadastrar Contato
      2 - Listar contatos
      3 - Consultar um registro
      4 - Editar um registro
      5 - Excluir um registro
""")
opcao = int(input("Digite a opção: "))
match opcao:
    case 1:
        cadastrar_contato()
    case 2:
        #consultar todos os registros
        lista_dados=list()

        cursor_consulta.execute("select * from contato")

        data = cursor_consulta.fetchall()

        if len(data) == 0:
            print("Não existem registros")
        else:

            for dt in data:
                lista_dados.append(dt)
            
            lista_dados = sorted(lista_dados)
            print(lista_dados)
            dados_df = pd.DataFrame.from_records(
                lista_dados, columns = ['id_contato', 'nome', 'instagram', 'email'], index = 'id_contato'
            )
            print(dados_df)

    case 3:
        #consultar parte dos registros
        lista_dados=list()
        id = int(input("Digite o ID: "))
        cursor_consulta.execute(f"select * from contato where id_contato = {id}")

        data = cursor_consulta.fetchall()

        if len(data) == 0:
            print("Não existe o registro")
        else:
            for dt in data:
                lista_dados.append(dt)

            lista_dados = sorted(lista_dados)

            dados_df = pd.DataFrame.from_records(
                lista_dados, columns = ['id_contato', 'nome', 'instagram', 'email'], index='id_contato'
            )
            print(dados_df)

    case 4:
        lista_dados=list()
        id = int(input("Digite o ID: "))
        cursor_consulta.execute(f"select * from contato id_contato = {id}")

        data = cursor_consulta.fetchall()

        if len(data) == 0:

            print("Não existe")
        else:

            for dt in data:
                lista_dados.append(dt)
            
            lista_dados = sorted(lista_dados)
            print(lista_dados)
            dados_df = pd.DataFrame.from_records(
                lista_dados, columns=['id_contato','nome', 'instagram','email'], index = 'id_contato'
            )
            print(dados_df) 



''' Script SQLSERVER
create database PythonSQL
use PythonSQL;
create table contato(
	id_contato int primary key,
	nome varchar(30),
	instagram varchar(30),
	email varchar(30),
)
'''