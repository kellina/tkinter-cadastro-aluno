from database import Database
from models.aluno import *

class AlunoRepositorio:
  def __init__(self):
    self.conn = Database()
    self.cur = conn.cursor()
    
      
  def inserir(self, aluno: Aluno):
    try:
      self.cur.execute("INSERT INTO alunos VALUES (?, ?, ?, ?, ?)",
                          (aluno.cod_aluno, aluno.nome, aluno.sexo, aluno.nascimento))
      self.conn.commit()
      print('Inserção realizada com sucesso')
    except:
      print('Erro ao realizar inserção.')
   
  def remover(self, aluno: Aluno):
    self.cur.execute("DELETE FROM alunos WHERE cod_aluno=?", (aluno.cod_aluno))
    self.conn.commit()

  def atualizar(self, aluno: Aluno):
    self.cur.execute("UPDATE alunos SET nome = ?, sexo = ?, nascimento = ? WHERE cod_aluno = ?",
                      (aluno.nome, aluno.sexo, aluno.nascimento), aluno.cod_aluno)
    self.conn.commit() 
 
  def selecionar_aluno(self, aluno: Aluno):
    self.cur.execute("SELECT * FROM alunos WHERE cod_aluno = ?", aluno.cod_aluno)
  
  def selecionar_todos_alunos (self):
    self.cur.execute("SELECT * FROM alunos ORDER BY nome").fetchall()

aluno_repositorio = AlunoRepositorio()