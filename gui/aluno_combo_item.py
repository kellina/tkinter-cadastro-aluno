class AlunoComboItem:
  def __init__(self, cod_aluno, nome):
    super().__init__()
    self.cod_aluno = cod_aluno
    self.nome = nome
    
  def __str__(self):
    return f"{self.cod_aluno} - {self.nome}"
