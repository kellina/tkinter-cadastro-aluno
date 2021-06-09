from .aluno import Aluno
from .disciplina import Disciplina

class NotaAluno:
  def notas(self, aluno, disciplina, nota):
    self.aluno = aluno
    self.disciplina = disciplina
    self.nota = nota
