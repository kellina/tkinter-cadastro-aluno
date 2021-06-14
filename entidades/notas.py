from database import db
from entidades.aluno import Aluno
from entidades.disciplina import Disciplina


class Nota:
  def __init__(self, cod_aluno, cod_disciplina, nota1, nota2, nota3, notaD):
    super().__init__()
    self.cod_aluno = cod_aluno
    self.cod_disciplina = cod_disciplina
    self.nota1 = nota1
    self.nota2 = nota2
    self.nota3 = nota3
    self.notaD = notaD
 
  def inserir(self):
    try:
      db.executeInsert("""INSERT INTO notas
                       (cod_aluno, cod_disciplina, nota_AV1, nota_AV2, nota_AV3, nota_AVD)
                       VALUES
                       (?, ?, ?, ?, ?, ?)""",
                      (self.cod_aluno, self.cod_disciplina, self.nota1, self.nota2, self.nota3, self.notaD))
      db.commit()
    except Exception as e:
      print(f'Erro ao realizar inserção: {e}')

  def atualizar(self):
    try:
      db.executeUpdate("""UPDATE notas 
                       SET nota_AV1 = ?, nota_AV2 = ?, nota_AV3 = ?, nota_AVD = ? 
                       WHERE cod_aluno = ?""",
                      (self.nota1, self.nota2, self.nota3, self.notaD, self.cod_aluno))
      db.commit() 
    except Exception as e:
      print('Erro ao realizar update.', e)
      
  @staticmethod
  def calcular_media(notas_do_aluno):
    try:
      notas_com_media = list()
      for nota_do_aluno in notas_do_aluno:
        notas_do_aluno_com_media = list(nota_do_aluno)
        notas = [nota_do_aluno[2], nota_do_aluno[3], nota_do_aluno[4], nota_do_aluno[5]]
        notas = sorted(notas)
        media = round((notas[1] + notas[2] + notas[3])/3,2)
        notas_do_aluno_com_media.append(media)
        notas_com_media.append(notas_do_aluno_com_media)
      return notas_com_media
    except Exception as e:
      print('Erro ao calcular média.', e)
  
  @staticmethod    
  def selecionar_nota_aluno_disciplina(cod_aluno, cod_disciplina):
    try:
      return db.executeSelectUm("""SELECT
                                notas.cod_aluno, notas.cod_disciplina,
                                notas.nota_AV1, notas.nota_AV2, notas.nota_AV3, notas.nota_AVD,
                                alunos.nome as nome_aluno, disciplinas.nome as nome_disciplina
                                FROM notas
                                INNER JOIN alunos ON (notas.cod_aluno = alunos.cod_aluno)
                                INNER JOIN disciplinas ON (notas.cod_disciplina = disciplinas.cod_disciplina)
                                WHERE notas.cod_aluno = ?
                                AND notas.cod_disciplina = ?""", (cod_aluno, cod_disciplina))
    except Exception as e:
      print('Erro ao realizar select.', e)
      
  @staticmethod
  def selecionar_todas_notas():
    try:
      notas = db.executeSelect("""SELECT
                              notas.cod_aluno, notas.cod_disciplina,
                              notas.nota_AV1, notas.nota_AV2, notas.nota_AVD, notas.nota_AV3,
                              alunos.nome as nome_aluno, disciplinas.nome as nome_disciplina
                              FROM notas
                              INNER JOIN alunos ON (notas.cod_aluno = alunos.cod_aluno)
                              INNER JOIN disciplinas ON (notas.cod_disciplina = disciplinas.cod_disciplina)""")
      return Nota.calcular_media(notas)
    except Exception as e:
      print('Erro ao realizar select.', e)
      
  @staticmethod   
  def remover_nota(cod_aluno, cod_disciplina):
    try:
      db.executeDelete("""DELETE FROM notas WHERE notas.cod_aluno = ?
                                AND notas.cod_disciplina = ?""", (cod_aluno, cod_disciplina))
      db.commit()
    except Exception as e:
      print('Erro ao realizar delete.', e)