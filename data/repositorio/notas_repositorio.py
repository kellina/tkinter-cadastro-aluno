import sqlite3
from data.models.nota import Nota

class NotaRepositorio:
  def __init__(self, nota: Nota):
    print('Metodo construtor')
    self.nota = Nota
    
  def abrirConexao(self):
    self.conn = sqlite3.connect()
    self.cur = self.conn.cursor()
    
    
  def inserir(self, nota: Nota):
    try:
      self.cur.execute("INSERT INTO notas VALUES (?, ?, ?)",
                      (self.cod_aluno, self.cod_disciplina, self.nota))
      self.conn.commit()
      print('Inserção realizada com sucesso')
    except:
      print('Erro ao realizar inserção.')
   
  def remover(self, nota: Nota):
    self.cur.execute("DELETE FROM notas WHERE cod_aluno=?", self.cod_aluno)
    self.conn.commit()

  def atualizar(self, nota: Nota):
    self.cur.execute("UPDATE notas SET nota = ? WHERE cod_aluno = ?",
                    (self.nota), self.cod_aluno)
    self.conn.commit() 

  def selecionar_aluno(self, nota: Nota):
    self.cur.execute("SELECT * FROM notas WHERE cod_disciplina = ?", self.cod_disciplina)
    self.conn.commit()
  
  def selecionar_todos_alunos (self, nota: Nota):
    self.cur.execute("SELECT * FROM notas").fetchall()
    self.conn.commit()