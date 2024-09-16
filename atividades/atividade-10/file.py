import mysql.connector

conn = mysql.connector.connect(
    host="192.168.0.27",
    user="myuser",
    password="mypassword",
    database="mydatabase"
)
cursor = conn.cursor()

def atualizar_status_aprovacao():

    cursor.execute("SELECT id_matricula, id_aluno, N1, N2, faltas FROM TB_MATRICULA")
    matriculas = cursor.fetchall()

    for matricula in matriculas:
        id_matricula, id_aluno, N1, N2, faltas = matricula
        aprovado_sn = True

        if faltas >= 20:
            aprovado_sn = False
        else:
            media = (N1 + N2) / 2
            if media < 6.0:
                aprovado_sn = False

        cursor.execute("""
            UPDATE TB_MATRICULA
            SET aprovado_sn = %s
            WHERE id_matricula = %s
        """, (aprovado_sn, id_matricula))
        print(f"Matricula {id_matricula}: Aluno {id_aluno} - Aprovado: {aprovado_sn}")
    
    conn.commit()

atualizar_status_aprovacao()

cursor.close()
conn.close()
