from tkinter import *                    
from tkinter import ttk
from tkinter import messagebox
from entidades.aluno import Aluno

class FrameAluno(ttk.Frame):
  def __init__(self, master=None, **kw): #construindo meu frame
    super().__init__(master=master, **kw)
    self.grid(column=0, row=0, sticky=(N, S, E, W))
    Grid.columnconfigure(self, 0, weight=1)
    # Sessão Formulário de cadastro
    self.nome_var = StringVar()
    self.sexo_var = StringVar()
    self.nascimento_var = StringVar()
    
    form_label_frame = ttk.Labelframe(self, text='Cadastro de Aluno')
    nome_label = ttk.Label(form_label_frame, text='Nome:')
    sexo_label = ttk.Label(form_label_frame, text='Sexo:')
    nascimento_label = ttk.Label(form_label_frame, text='Nascimento:')
    
    nome_entry = ttk.Entry(form_label_frame, textvariable=self.nome_var)
    nascimento_entry = ttk.Entry(form_label_frame, textvariable=self.nascimento_var)
    sexo_m_radio = ttk.Radiobutton(form_label_frame, text='Masculino', value='M', variable=self.sexo_var)
    sexo_f_radio = ttk.Radiobutton(form_label_frame, text='Feminino', value='F', variable=self.sexo_var)
    btn_salvar = ttk.Button(form_label_frame, text='Salvar', command=lambda: self.salvar_aluno())
    
    # Sessão Listagem de alunos cadastrados
    listagem_label_frame = ttk.Labelframe(self, text='Alunos Cadastrados')
        
    btn_incluir = ttk.Button(listagem_label_frame, text='Incluir')
    btn_alterar = ttk.Button(listagem_label_frame, text='Alterar')
    btn_excluir = ttk.Button(listagem_label_frame, text='Excluir')
    
    
    # Alinhamento dos componentes
    form_label_frame.grid(column=0, row=0, sticky=(E, W), padx=10, pady=10)
    nome_label.grid(column=0, row=0, pady=5, padx=5, sticky=E)
    nome_entry.grid(column=1, row=0, columnspan=2, sticky = (W, E), pady=5)
    nascimento_label.grid(column=0, row=1, pady=5, padx=5, sticky=E)
    nascimento_entry.grid(column=1, row=1, columnspan=2, sticky = (W, E), pady=5)
    sexo_label.grid(column=0, row=2, padx=5, sticky=E)
    sexo_m_radio.grid(column=1, row=2, padx=5)
    sexo_f_radio.grid(column=2, row=2, padx=5)
    btn_salvar.grid(column=2, row=3, pady=5)
    
    listagem_label_frame.grid(column=0, row=1, sticky=(E, W), pady=10, padx=10)
    
    #alunos = aluno_repositorio.selecionar_todos_alunos()
    alunos = [
      ('João Batista', 'Masculino', '10/01/1992'),
      ('Maria Eduarda', 'Feminino', '15/03/1992'),
      ('Pedro Arthur', 'Masculino', '20/05/1992'),
      ('Ana Laura', 'Feminino', '22/08/1992')]
    
    colunas = ('#1', '#2', '#3')
    tree = ttk.Treeview(listagem_label_frame, columns=colunas, height=4, show='headings')
    tree.heading('#1', text='Nome')
    tree.heading('#2', text='Sexo')
    tree.heading('#3', text='Nascimento')
    tree.column('#3', anchor='center')
    for aluno in alunos:
      tree.insert('', 'end', values=aluno)
    
    # Add Scrollbar
    scrollbar = ttk.Scrollbar(listagem_label_frame, orient=VERTICAL, command=tree.yview)
    tree.configure(yscroll=scrollbar.set, height=4)
    
    tree.grid(column=0, row=0, columnspan=3, padx=(5, 0), pady=5, sticky=(E, W))
    scrollbar.grid(column=3, row=0, sticky=(N, S), padx=(0, 5))
    btn_incluir.grid(column=0, row=1, pady=(0, 5))
    btn_alterar.grid(column=1, row=1)
    btn_excluir.grid(column=2, row=1)    
  
  def salvar_aluno(self):
    print("Salvando aluno")
    aluno = Aluno(self.nome_var.get(), self.sexo_var.get(), self.nascimento_var.get())
    aluno.inserir()
    messagebox.showinfo(message=f'Aluno {self.nome_var.get()} inserido com sucesso!')
    self.limpar_formulario()
    
  def limpar_formulario(self):
    self.nome_var.set("")
    self.sexo_var.set("")
    self.nascimento_var.set("")