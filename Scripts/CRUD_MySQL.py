import mysql.connector # pip install mysql-connector
from rich import print # pip install rich

# <table> users 
#   <column> id INT(10) AUTO_INCREMENT NOT NULL PRIMARY KEY </column>
#   <column> nome VARCHAR(255) </column>
#   <column> idade INT(3) </column>
# </table>

try:
    conn = mysql.connector.connect(host = 'localhost', user = 'root_depuracao', password = 'root_depuracao', database = 'proj_1', charset = 'utf8')
    cursor  = conn.cursor(dictionary = True)

    print("[green][1] - :memo: CADASTRAR[/]\n[red][2] - :x: DELETAR[/]\n[cyan][3] - :mag: CONSULTAR[/]\n[yellow][4] - [/]:pen:[yellow] ALTERAR[/]")
    opcao = input('Digite o procedimento desejado: ')
# ==================== CADASTRAR ====================
    if opcao == '1':
        nome = input('Digite um nome: ')
        idade = input('Digite uma idade: ')

        cursor.execute(f"INSERT INTO users(nome, idade) VALUES ('{nome}', {idade})")
        print('[green]CADASTRO REALIZADO COM SUCESSO![/]')
# ==================== DELETAR ====================
    elif opcao  == '2':
        id = input('Digite o ID que sera excluido: ')
        
        cursor.execute(f"SELECT nome FROM users WHERE id = {id}")
        print("[white]"+cursor.fetchall()+"[/]")
        # ==================== CONFIRMAÇÃO DE PROCEDIMENTO ====================
        opcao_delete = input('[S/N] - Deseja realmente excluir esse registro? ').upper()

        if opcao_delete == 'S':
            cursor.execute(f"DELETE FROM users WHERE id = {id}")
            print('[red]REGISTRO EXCLUIDO COM SUCESSO![/]')
        else:
            print('[red]FIM DO PROGRAMA![/]')
# ==================== CONSULTAR ====================
    elif opcao == '3':
        opcao_query = input('[1] - Consultar Registro Unico por ID\n[2] - Consultar Registros por Idade\n[3] - Consultar Todos os Registros\nDigite o procedimento desejado: ')
        # ==================== REGISTRO UNICO POR ID ====================
        if opcao_query == '1':
            id = input('Digite o ID que devera ser consultado: ')

            cursor.execute(f"SELECT * FROM users WHERE id = {id}")
            print(f"[cyan]{cursor.fetchall()}[/]")
            print('[red]FIM DO PROGRAMA![/]')
        # ==================== REGISTRO POR IDADE ====================
        elif opcao_query == '2':
            idade = input('Digite a idade que devera ser consultado: ')

            cursor.execute(f"SELECT * FROM users WHERE idade = {idade}")
            users = cursor.fetchall()

            for i in range(len(users)):
                print(f"[cyan]{users[i]}[/]")
            print('[red]FIM DO PROGRAMA![/]')
        # ==================== TODOS OS REGISTROS ====================
        elif opcao_query == '3':
            cursor.execute(f"SELECT * FROM users")
            users = cursor.fetchall()

            for i in range(len(users)):
                print(f"[cyan]{users[i]}[/]")
            print('[red]FIM DO PROGRAMA![/]')
        # ==================== DEFAULT ====================
        else:
            print('[red]OPÇÃO INVALIDA, PROCESSO INTERROMPIDO![/]')
# ==================== ALTERAR ====================
    elif opcao == '4':
        opcao_update = input('[1] - Alterar Nome\n[2] - Alterar Idade\nQual Informação Deseja Modificar? ')
        id = input('Digite o ID do registro que recebera alterações: ')
        # ==================== ALTERAR NOME ====================
        if opcao_update == '1':
            nome = input('Digite um nome: ')

            cursor.execute(f"UPDATE users SET nome = '{nome}' WHERE id = {id}")
            print('[purple]REGISTRO ALTERADO COM SUCESSO![/]')
            print('[red]FIM DO PROGRAMA![/]')
        # ==================== ALTERAR IDADE ====================
        elif opcao_update == '2':
            idade = input('Digite uma idade: ')

            cursor.execute(f"UPDATE users SET nome = {idade} WHERE id = {id}")
            print('[purple]REGISTRO ALTERADO COM SUCESSO![/]')
            print('[red]FIM DO PROGRAMA![/]')
        # ==================== DEFAULT ====================
        else:
            print('[red]OPÇÃO INVALIDA, PROCESSO INTERROMPIDO![/]')
# ==================== DEFAULT ====================
    else:
        print('[red]OPÇÃO INVALIDA, PROCESSO INTERROMPIDO![/]')
    # ==================== CONCLUSÃO DA CONEXÃO ====================
    conn.commit()
    conn.close()
except:
    print('[red]FALHA NA EXECUÇÃO DO PROGRAMA, PROCESSO INTERROMPIDO![/]')
    conn.close()