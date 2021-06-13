from database import db

class Aluno:
  def __init__(self, nome, sexo, nascimento):
    super().__init__()
    self.cod_aluno = None
    self.nome = nome
    self.sexo = sexo
    self.nascimento = nascimento

  def inserir(self):
    try:
      id = db.executeInsert("INSERT INTO alunos(nome, sexo, nascimento) VALUES (?, ?, ?)",
                          (self.nome, self.sexo, self.nascimento))
      db.commit()
      self.cod_aluno = id
      print('Inserção realizada com sucesso')
    except Exception as e:
      print(f'Erro ao realizar inserção: {e}.')
   
  def remover_aluno(self):
    nome = self.nome.get()
    db.executeQuery("DELETE FROM alunos WHERE nome=?", (nome))
    db.commit()

  def atualizar_aluno(self):
    nome = self.nome.get()
    sexo = self.sexo.get()
    nascimento = self.nascimento.get()
    db.execute("UPDATE alunos SET nome = ?, sexo = ?, nascimento = ? WHERE nome = ?",
                      (nome, sexo, nascimento), nome)
    db.commit() 
 
  def selecionar_aluno(self):
    nome = self.nome.get()
    db.executeQuery("SELECT * FROM alunos WHERE nome = ?", nome)
  
  def selecionar_todos_alunos (self):
    return db.executeQuery("SELECT * FROM alunos ORDER BY nome")
