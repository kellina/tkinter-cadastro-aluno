import sqlite3
from data.models.aluno import Aluno

class AlunoRepositorio:
  def __init__(self, aluno: Aluno):
    print('Metodo construtor')
    self.aluno = Aluno
    
  def abrirConexao(self):
    self.conn = sqlite3.connect()
    self.cur = self.conn.cursor()
    
    
  def inserir(self, aluno: Aluno):
    try:
      self.cur.execute("INSERT INTO alunos VALUES (?, ?, ?, ?, ?)",
                          (self.cod_aluno, self.nome, self.sexo, self.nascimento, self.curso))
      self.conn.commit()
      print('Inserção realizada com sucesso')
    except:
      print('Erro ao realizar inserção.')
   
  def remover(self, aluno: Aluno):
    self.cur.execute("DELETE FROM alunos WHERE cod_aluno=?", (self.cod_aluno))
    self.conn.commit()

  def atualizar(self, aluno: Aluno):
    self.cur.execute("UPDATE alunos SET nome = ?, sexo = ?, nascimento = ?, curso = ? WHERE cod_aluno = ?",
                      (self.nome, self.sexo, self.nascimento, self.curso), self.cod_aluno)
    self.conn.commit() 

    
  def selecionar_aluno(self, aluno: Aluno):
    self.cur.execute("SELECT * FROM alunos WHERE cod_aluno = ?", self.cod_aluno)
    self.conn.commit()
  
  def selecionar_todos_alunos (self, aluno: Aluno):
    self.cur.execute("SELECT * FROM alunos").fetchall()
    self.conn.commit()