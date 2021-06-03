import sqlite3
from data.models.disciplina import Disciplina

class DisciplinaRepositorio:
  def __init__(self, disciplina: Disciplina):
    print('Metodo construtor')
    self.disciplina = Disciplina
    
  def abrirConexao(self):
    self.conn = sqlite3.connect()
    self.cur = self.conn.cursor()
    
    
  def inserir(self, disciplina: Disciplina):
    try:
      self.cur.execute("INSERT INTO disciplinas VALUES (?, ?, ?, ?)",
                      (self.cod_disciplina, self.nome, self.carga_horaria, self.descricao))
      self.conn.commit()
      print('Inserção realizada com sucesso')
    except:
      print('Erro ao realizar inserção.')
   
  def remover(self, disciplina: Disciplina):
    self.cur.execute("DELETE FROM disciplinas WHERE cod_disciplina=?", (self.cod_disciplina))
    self.conn.commit()

  def atualizar(self, disciplina: Disciplina):
    self.cur.execute("UPDATE disciplinas SET nome = ?, carga_horaria = ?, descricao = ? WHERE cod_disciplina = ?",
                    (self.nome, self.carga_horaria, self.descricao), self.cod_disciplina)
    self.conn.commit() 

  def selecionar_aluno(self, disciplina: Disciplina):
    self.cur.execute("SELECT * FROM disciplinas WHERE cod_disciplina = ?", self.cod_disciplina)
    self.conn.commit()
  
  def selecionar_todos_alunos (self, disciplina: Disciplina):
    self.cur.execute("SELECT * FROM disciplinas").fetchall()
    self.conn.commit()