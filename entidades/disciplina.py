from database import db

class Disciplina:
  def __init__(self, nome, carga_horaria, descricao):
    super().__init__()
    self.cod_disciplina = None
    self.nome = nome
    self.carga_horaria = carga_horaria
    self.descricao = descricao
    
  def inserir(self):
    try:
      db.executeInsert("INSERT INTO disciplinas(nome, carga_horaria, descricao) VALUES (?, ?, ?)",
                      (self.nome, self.carga_horaria, self.descricao))
      db.commit()
      self.cod_disciplina = id
    except Exception as e:
      print('Erro ao realizar inserção.', e)
   
  def atualizar(self):
    try:
      db.executeUpdate("UPDATE disciplinas SET nome = ?, carga_horaria = ?, descricao = ? WHERE cod_disciplina = ?",
                      (self.nome, self.carga_horaria, self.descricao, self.cod_disciplina))
      db.commit() 
    except Exception as e:
      print('Erro ao realizar update.', e)

  @staticmethod
  def selecionar_uma(cod_disciplina):
    try:
      return db.executeSelectUm("SELECT cod_disciplina, nome, carga_horaria, descricao FROM disciplinas WHERE cod_disciplina = ?", cod_disciplina)
    except Exception as e:
      print('Erro ao realizar select.', e)
      
  @staticmethod
  def selecionar_todas():
    try:
      return db.executeSelect("SELECT cod_disciplina, nome, carga_horaria, descricao FROM disciplinas ORDER BY nome")
    except Exception as e:
      print('Erro ao realizar select.', e)
      
  @staticmethod
  def remover(cod_disciplina):
    try:
      db.executeDelete("DELETE FROM disciplinas WHERE cod_disciplina=?", cod_disciplina)
      db.commit()
    except Exception as e:
      print('Erro ao realizar delete.', e)