import sqlite3


class Database:
    def __init__(self):
        self.conn = sqlite3.connect('alunos.db')
        self.cur = self.conn.cursor()
        self.cur.execute(
            """CREATE TABLE IF NOT EXISTS alunos (
                cod_aluno integer primary key not null, 
                nome text not null, 
                sexo text not null,
                nascimento texto not null
                )""")
        self.conn.commit()
        self.cur.execute(
            """CREATE TABLE IF NOT EXISTS disciplinas (
                cod_disciplina integer primary key not null, 
                nome text not null, 
                carga_horaria text not null,
                descricao texto not null
                )""")
        self.conn.commit()
        self.cur.execute(
            """CREATE TABLE IF NOT EXISTS notas (
                cod_aluno integer, 
                cod_disciplina integer, 
                nota real not null,
                foreign key(cod_aluno) REFERENCES alunos(cod_aluno),
                foreign key(cod_disciplina) REFERENCES disciplinas(cod_disciplina)
                )""")
        self.conn.commit()
    
    def __del__(self):
        self.conn.close()
        
database = Database()
