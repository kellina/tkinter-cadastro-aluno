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
            id = db.executeInsert(
                "INSERT INTO alunos(nome, sexo, nascimento) VALUES (?, ?, ?)",
                  (self.nome, self.sexo, self.nascimento)
            )
            db.commit()
            self.cod_aluno = id
        except Exception as e:
            print(f"Erro ao realizar inserção: {e}.")

    def atualizar(self):
        try:
            db.executeUpdate(
                "UPDATE alunos SET nome = ?, sexo = ?, nascimento = ? WHERE cod_aluno = ?",
                  (self.nome, self.sexo, self.nascimento, self.cod_aluno),
            )
            db.commit()
        except Exception as e:
            print(f"Erro ao realizar update: {e}.")

    @staticmethod
    def selecionar_um(cod_aluno):
        try:
            return db.executeSelectUm(
                "SELECT cod_aluno, nome, sexo, nascimento FROM alunos WHERE cod_aluno = ?", cod_aluno
            )
        except Exception as e:
            print(f"Erro ao realizar select: {e}.")

    @staticmethod
    def selecionar_todos():
        try:
            return db.executeSelect("SELECT cod_aluno, nome, sexo, nascimento FROM alunos ORDER BY nome")
        except Exception as e:
            print(f"Erro ao realizar select: {e}.")

    @staticmethod
    def remover(cod_aluno):
        try:
            db.executeDelete("DELETE FROM alunos WHERE cod_aluno=?", cod_aluno)
            db.commit()
        except Exception as e:
            print(f"Erro ao realizar delete: {e}.")
