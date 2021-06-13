import sqlite3
from database import db

class DisciplinaRepositorio:
    
  def inserir_disciplina(self):
    nome=self.nome.get()
    carga_horaria=self.carga_horaria.get()
    descricao=self.descricao.get()
    try:
      db.executeQuery("INSERT INTO disciplinas VALUES (?, ?, ?)",
                      (nome, carga_horaria, descricao))
    except:
      print('Erro ao realizar inserção.')
    self.conn.commit()
    print('Inserção realizada com sucesso')
   
  def remover_disciplina(self):
    nome=self.nome.get()
    db.executeQuery("DELETE FROM disciplinas WHERE nome=?", nome)
    self.conn.commit()

  def atualizar_disciplina(self):
    nome=self.nome.get()
    carga_horaria=self.carga_horaria.get()
    descricao=self.descricao.get()
    db.executeQuery("UPDATE disciplinas SET nome = ?, carga_horaria = ?, descricao = ? WHERE nome = ?",
                    (nome, carga_horaria, descricao), nome)
    self.conn.commit() 

  def selecionar_disciplina(self):
    nome=self.nome.get()
    db.executeQuery("SELECT * FROM disciplinas WHERE nome = ?", nome)
    self.conn.commit()
  
  def selecionar_todas_disciplinas (self):
    db.executeQuery("SELECT * FROM disciplinas")
    self.conn.commit()