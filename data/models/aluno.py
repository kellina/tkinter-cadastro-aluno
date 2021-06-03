from data.models.nota_aluno import NotaAluno

class Aluno:
  def __init__(self, cod_aluno, nome, sexo, nascimento, notas: list[NotaAluno]):
    self.cod_aluno = cod_aluno
    self.nome = nome
    self.sexo = sexo
    self.nascimento = nascimento
    self.notas = notas