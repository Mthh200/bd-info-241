import sqlite3

conn = sqlite3.connect('dbalunos.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS TB_ALUNO (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        aluno_nome TEXT NOT NULL,
        endereco TEXT NOT NULL
    );
''')

conn.close()