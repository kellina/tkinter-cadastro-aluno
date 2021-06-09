import sqlite3
from models.nota_aluno import *

class NotaRepositorio:
  def __init__(self, nota: NotaAluno):
    print('Metodo construtor')
    self.nota = NotaAluno
    
  def abrirConexao(self):
    self.conn = sqlite3.connect()
    self.cur = self.conn.cursor()
    
    
  def inserir(self, nota: NotaAluno):
    try:
      self.cur.execute("INSERT INTO notas VALUES (?, ?, ?)",
                      (nota.aluno.id, nota.disciplina.id, nota.nota))
      self.conn.commit()
      print('Inserção realizada com sucesso')
    except:
      print('Erro ao realizar inserção.')
   
  def remover(self, nota: NotaAluno):
    self.cur.execute("DELETE FROM notas WHERE cod_aluno=?", nota.aluno.id)
    self.conn.commit()

  def atualizar(self, nota: NotaAluno):
    self.cur.execute("UPDATE notas SET nota = ? WHERE cod_aluno = ?",
                    (nota.nota), nota.aluno.id)
    self.conn.commit() 

  def selecionar_aluno(self, nota: NotaAluno):
    self.cur.execute("SELECT * FROM notas WHERE cod_disciplina = ?", nota.disciplina.id)
    self.conn.commit()
  
  def selecionar_todos_alunos (self, nota: NotaAluno):
    self.cur.execute("SELECT * FROM notas").fetchall()
    self.conn.commit()