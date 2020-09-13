'''
O seguinte script é responsável pela conexão com o banco de dados SQL SERVER, e por armazenar o resultado de pesquisa em forma de dicionário, com o nome dos campos e seus respectivos valores.
'''

# Execute o comando abaixo para baixar a biblioteca pyodbc
# pip install pyodbc

import pyodbc
server = ""
database = "" 
username = ""
password = ""

# Acesse o seguinte link para obter o ODBC Driver 11 para SQL Server:
# https://www.microsoft.com/pt-br/download/details.aspx?id=36434
# Acesse o seguinte link para saber como configurá-lo:
# https://docs.microsoft.com/pt-br/sql/integration-services/import-export-data/connect-to-an-odbc-data-source-sql-server-import-and-export-wizard?view=sql-server-ver15
# Sinta-se a vontade para escolher qual versão utilizar.

# String de conexão conforme é informado no link passado.
stringConexao = 'Driver={SQL Server Native Client 11.0};Server='+server+';DataBase='+database+';UID='+username+';PWD='+password

# Tenta executar conexão com o banco. As excessões serão printadas no console!
statusConexao = False
try:
    conexao = pyodbc.connect(stringConexao)
    cursor = conexao.cursor()
    statusConexao = True
except Exception as err:
    print('Tipo de Erro: ', type(err))
    print('Argumentos:')
    for argumento in err.args:
        print(argumento)

# Se houver conexão, executa a query...
if statusConexao == True:
    try:
        queryColunas = cursor.execute(""" SELECT COLUMN_NAME 
                                        FROM INFORMATION_SCHEMA.COLUMNS 
                                        WHERE TABLE_NAME = 'NomeDaTabela' """)
        # Encapsula os dados em formato de lista.
        queryColunas = queryColunas.fetchall()
        # Aqui é onde o nosso dicionário é criado.
        query = {}
        # Para cada coluna, será adicinada uma nova key dentro de nosso dicionário, com uma lista como valor, para inserção posterior.
        for coluna in queryColunas:
            query.update({coluna[0]:[]})
        queryValores = cursor.execute(""" SELECT *
                                        FROM NomeDaTabela """)
        # Encapsula os dados em formato de lista.
        queryValores = queryValores.fetchall()
        # Adiciona os valores da query conforme o nome da coluna.
        for valor in queryValores:
            cont = 0
            for valorColuna in query.values():
                valorColuna.append(valor[cont])
                cont += 1
        cursor.close()

    # Caso ocorra algum erro com as querys, será printado no console!
    except Exception as err:
        print('Tipo: ', type(err))
        print('Argumentos:')
        for argumento in err.args:
            print(argumento)
