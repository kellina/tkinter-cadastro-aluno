import sqlite3
from repositorio.aluno_repositorio import AlunoRepositorio
from repositorio.disciplina_repositorio import DisciplinaRepositorio
from database import db

class NotaRepositorio:
 
  def inserir_nota(self):
    cod_aluno=self.cod_aluno.get()
    cod_disciplina=self.cod_disciplina.get()
    notaAV1=self.notaAV1.get()
    notaAV2=self.notaAV2.get()
    notaAV3=self.notaAV3.get()
    notaAVD=self.notaAVD.get()
    try:
      db.executeQuery("INSERT INTO notas VALUES (?, ?, ?, ?, ?, ?)",
                      (cod_aluno, cod_disciplina, notaAV1, notaAV2, notaAV3, notaAVD))
    except:
      print('Erro ao realizar inserção.')
    self.conn.commit()
    print('Inserção realizada com sucesso')
   
  def remover_nota(self):
    cod_aluno=self.cod_aluno.get()
    db.executeQuery("DELETE FROM notas WHERE cod_aluno=?", cod_aluno)
    self.conn.commit()

  def atualizar_nota(self):
    cod_aluno=self.cod_aluno.get()
    notaAV1=self.notaAV1.get()
    notaAV2=self.notaAV2.get()
    notaAV3=self.notaAV3.get()
    notaAVD=self.notaAVD.get()
    db.executeQuery("UPDATE notas SET notaAV1 = ?, notaAV2 = ?, notaAV3 = ?, notaAVD = ? WHERE cod_aluno = ?",
                    (notaAV1, notaAV2, notaAV3, notaAVD), cod_aluno)
    self.conn.commit() 

  def selecionar_notas_disciplina(self):
    cod_disciplina=self.cod_disciplina.get()
    db.executeQuery("SELECT * FROM notas WHERE cod_disciplina = ?", cod_disciplina)
    self.conn.commit()
  
  def selecionar_todas_notas (self):
    db.executeQuery("SELECT * FROM notas")
    self.conn.commit()