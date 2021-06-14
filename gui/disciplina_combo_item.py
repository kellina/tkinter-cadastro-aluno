class DisciplinaComboItem:
  def __init__(self, cod_disciplina, nome):
    super().__init__()
    self.cod_disciplina = cod_disciplina
    self.nome = nome
    
  def __str__(self):
    return f"{self.cod_disciplina} - {self.nome}"
