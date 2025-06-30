import mysql.connector

def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="sua_senha",
        database="wayne"
    )

def verificar_usuario(usuario, senha):
    db = conectar()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE nome = %s AND senha = %s", (usuario, senha))
    resultado = cursor.fetchone()
    db.close()
    return resultado is not None