#python -m venv venv
#.\venv\Scripts\activate
#pip install pandas

from flask import Flask
import pandas as pd
import mysql.connector

# Criar uma conexão com o banco de dados MySQL
conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="ubermensch",
    database="db_green_world"
)

# Dados a serem inseridos na tabela tbl_semente
dados_semente = {
    'nome': ['Nome da Semente'],
    'quantidade_agua_por_regada': ['100 ml'],
    'regadas_por_semana': ['3 vezes'],
    'tempo_cultivo': [10],
    'recomendacoes': ['Recomendações para o cultivo']
}
df_semente = pd.DataFrame(dados_semente)

# Criar o cursor para executar as consultas SQL
cursor = conexao.cursor()

# Inserir dados na tabela tbl_semente
for _, row in df_semente.iterrows():
    sql = "INSERT INTO tbl_semente (nome, quantidade_agua_por_regada, regadas_por_semana, tempo_cultivo, recomendacoes) VALUES (%s, %s, %s, %s, %s)"
    valores = (
        row['nome'],
        row['quantidade_agua_por_regada'],
        row['regadas_por_semana'],
        row['tempo_cultivo'],
        row['recomendacoes']
    )
    cursor.execute(sql, valores)

# Confirmar as alterações no banco de dados
conexao.commit()

# Fechar o cursor e a conexão
cursor.close()
conexao.close()
