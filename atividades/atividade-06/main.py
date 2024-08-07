from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3
from models import conn, cursor

app = FastAPI()

# Definir a entidade aluno
class Aluno(BaseModel):
    id: int
    aluno_nome: str
    endereco: str

# Endpoint para criar um aluno
@app.post("/criar_aluno")
async def criar_aluno(aluno: Aluno):
    cursor.execute('''
        INSERT INTO TB_ALUNO (aluno_nome, endereco)
        VALUES (?, ?);
    ''', (aluno.aluno_nome, aluno.endereco))
    conn.commit()
    return {"mensagem": "Aluno criado com sucesso"}

# Endpoint para listar todos os alunos
@app.get("/listar_alunos")
async def listar_alunos():
    cursor.execute('''
        SELECT * FROM TB_ALUNO;
    ''')
    alunos = cursor.fetchall()
    return [{"id": aluno[0], "aluno_nome": aluno[1], "endereco": aluno[2]} for aluno in alunos]

# Endpoint para listar um aluno
@app.get("/listar_um_aluno/{id}")
async def listar_um_aluno(id: int):
    cursor.execute('''
        SELECT * FROM TB_ALUNO
        WHERE id = ?;
    ''', (id,))
    aluno = cursor.fetchone()
    if aluno is None:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")
    return {"id": aluno[0], "aluno_nome": aluno[1], "endereco": aluno[2]}

# Endpoint para atualizar um aluno
@app.put("/atualizar_aluno/{id}")
async def atualizar_aluno(id: int, aluno: Aluno):
    cursor.execute('''
        UPDATE TB_ALUNO
        SET aluno_nome = ?, endereco = ?
        WHERE id = ?;
    ''', (aluno.aluno_nome, aluno.endereco, id))
    conn.commit()
    return {"mensagem": "Aluno atualizado com sucesso"}

# Endpoint para excluir um aluno
@app.delete("/excluir_aluno/{id}")
async def excluir_aluno(id: int):
    cursor.execute('''
        DELETE FROM TB_ALUNO
        WHERE id = ?;
    ''', (id,))
    conn.commit()
    return {"mensagem": "Aluno excluído com sucesso"}