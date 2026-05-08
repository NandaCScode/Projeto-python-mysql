import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="SUA SENHA",
    database="estudos"
)

cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS tarefas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    status VARCHAR(20)
)
""")

nome_tarefa = input("Digite uma tarefa: ")

cursor.execute("""
INSERT INTO tarefas (nome, status)
VALUES (%s, %s)
""", (nome_tarefa, "Pendente"))

conexao.commit()

cursor.execute("SELECT * FROM tarefas")

resultado = cursor.fetchall()

for tarefa in resultado:
    print(f"""
ID: {tarefa[0]}
Tarefa: {tarefa[1]}
Status: {tarefa[2]}
""")
    
