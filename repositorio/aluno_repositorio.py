from database import db
class AlunoRepositorio:
      
  def inserir_aluno(self):
    nome = self.nome.get()
    sexo = self.sexo.get()
    nascimento = self.nascimento.get()
    try:
      db.executeQuery("INSERT INTO alunos VALUES (?, ?, ?)",
                          (nome, sexo, nascimento))
    except:
      print('Erro ao realizar inserção.')
    db.commit()
    print('Inserção realizada com sucesso')
   
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

aluno_repositorio = AlunoRepositorio()