import sqlite3

from typing import Iterable

class Database:
    def __init__(self):
        self.conn = sqlite3.connect('alunos.db')
        self.cur = self.conn.cursor()
        self.cur.execute(
            """CREATE TABLE IF NOT EXISTS alunos (
                cod_aluno integer primary key autoincrement, 
                nome text not null, 
                sexo text not null,
                nascimento texto not null
                )""")
        self.conn.commit()
        self.cur.execute(
            """CREATE TABLE IF NOT EXISTS disciplinas (
                cod_disciplina integer primary key autoincrement, 
                nome text not null, 
                carga_horaria text not null,
                descricao texto not null
                )""")
        self.conn.commit()
        self.cur.execute(
            """CREATE TABLE IF NOT EXISTS notas (
                cod_aluno integer, 
                cod_disciplina integer, 
                nota_AV1 real not null,
                nota_AV2 real not null,
                nota_AV3 real not null,
                nota_AVD real not null,
                foreign key(cod_aluno) REFERENCES alunos(cod_aluno),
                foreign key(cod_disciplina) REFERENCES disciplinas(cod_disciplina)
                )""")
        self.conn.commit()
    
    def __del__(self):
        self.conn.close()
    
    def executeSelect(self, sql: str, seq_of_parameters: Iterable[Iterable]=[]):
        return self.cur.execute(sql, seq_of_parameters).fetchall()
    
    def executeSelectUm(self, sql: str, seq_of_parameters: Iterable[Iterable]=[]):
        return self.cur.execute(sql, seq_of_parameters).fetchone()
    
    def executeInsert(self, sql: str, seq_of_parameters: Iterable[Iterable]):
        return self.cur.execute(sql, seq_of_parameters).lastrowid
    
    def executeUpdate(self, sql: str, seq_of_parameters: Iterable[Iterable]=[]):
        return self.cur.execute(sql, seq_of_parameters)
    
    def executeDelete(self, sql: str, seq_of_parameters: Iterable[Iterable]):
        return self.cur.execute(sql, seq_of_parameters)
    
    def commit(self):
        self.conn.commit()

db = Database()
