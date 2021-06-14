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
    self.cod_aluno = None
    self.nome_var = StringVar()
    self.sexo_var = StringVar()
    self.nascimento_var = StringVar()
    
    form_label_frame = ttk.Labelframe(self, text='Cadastro de Aluno')
    nome_label = ttk.Label(form_label_frame, text='Nome:')
    sexo_label = ttk.Label(form_label_frame, text='Sexo:')
    nascimento_label = ttk.Label(form_label_frame, text='Nascimento:')
    
    self.nome_entry = ttk.Entry(form_label_frame, textvariable=self.nome_var)
    nascimento_entry = ttk.Entry(form_label_frame, textvariable=self.nascimento_var)
    sexo_m_radio = ttk.Radiobutton(form_label_frame, text='Masculino', value='M', variable=self.sexo_var)
    sexo_f_radio = ttk.Radiobutton(form_label_frame, text='Feminino', value='F', variable=self.sexo_var)
    btn_salvar = ttk.Button(form_label_frame, text='Salvar', command=lambda: self.salvar_aluno())
    
    # Sessão Listagem de alunos cadastrados
    listagem_label_frame = ttk.Labelframe(self, text='Alunos Cadastrados')
        
    btn_incluir = ttk.Button(listagem_label_frame, text='Incluir',
                             command=lambda: self.incluir_aluno())
    btn_alterar = ttk.Button(listagem_label_frame, text='Alterar',
                             command=lambda: self.alterar_aluno(self.tree.focus()))
    btn_excluir = ttk.Button(listagem_label_frame, text='Excluir',
                             command=lambda: self.excluir_aluno(self.tree.focus()))
       
    # Alinhamento dos componentes
    form_label_frame.grid(column=0, row=0, sticky=(E, W), padx=10, pady=10)
    nome_label.grid(column=0, row=0, pady=5, padx=5, sticky=E)
    self.nome_entry.grid(column=1, row=0, columnspan=2, sticky = (W, E), pady=5)
    nascimento_label.grid(column=0, row=1, pady=5, padx=5, sticky=E)
    nascimento_entry.grid(column=1, row=1, columnspan=2, sticky = (W, E), pady=5)
    sexo_label.grid(column=0, row=2, padx=5, sticky=E)
    sexo_m_radio.grid(column=1, row=2, padx=5)
    sexo_f_radio.grid(column=2, row=2, padx=5)
    btn_salvar.grid(column=2, row=3, pady=5)
    
    listagem_label_frame.grid(column=0, row=1, sticky=(E, W), pady=10, padx=10)
    
    colunas = ('#1', '#2', '#3')
    self.tree = ttk.Treeview(listagem_label_frame, columns=colunas, height=4, show='headings')
    self.tree.heading('#1', text='Nome')
    self.tree.heading('#2', text='Sexo')
    self.tree.heading('#3', text='Nascimento')
    self.tree.column('#3', anchor='center')
    
    self.popular_tree()
      
    # Add Scrollbar
    scrollbar = ttk.Scrollbar(listagem_label_frame, orient=VERTICAL, command=self.tree.yview)
    self.tree.configure(yscroll=scrollbar.set, height=4)
    
    self.tree.grid(column=0, row=0, columnspan=3, padx=(5, 0), pady=5, sticky=(E, W))
    scrollbar.grid(column=3, row=0, sticky=(N, S), padx=(0, 5))
    btn_incluir.grid(column=0, row=1, pady=(0, 5))
    btn_alterar.grid(column=1, row=1)
    btn_excluir.grid(column=2, row=1)
  
  def popular_tree(self):
    alunos = Aluno.selecionar_todos()
    self.limpar_tree()
    for aluno in alunos:
      aluno = list(aluno)
      if(aluno[2] == "M"):
        aluno[2] = "Masculino"
      else:
        aluno[2] = "Feminino"
      self.tree.insert('', index='end', iid=aluno[0], values=aluno[1:])
    
  def limpar_tree(self):
    for i in self.tree.get_children():
      self.tree.delete(i)
  
  def salvar_aluno(self):
    print("Salvando aluno")
    aluno = Aluno(self.nome_var.get(), self.sexo_var.get(), self.nascimento_var.get())
    if(self.cod_aluno == None):
      aluno.inserir()
      messagebox.showinfo(title='Informação', message=f'Aluno {self.nome_var.get()} inserido com sucesso!')
    else:
      aluno.cod_aluno = self.cod_aluno
      aluno.atualizar()
      messagebox.showinfo(title='Informação', message=f'Aluno {self.nome_var.get()} alterado com sucesso!')
    self.limpar_formulario()
    self.popular_tree()
    
  def alterar_aluno(self, id):
    if(id == ''):
      messagebox.showwarning(title='Alerta', message='Selecione um aluno')
    else:
      aluno = Aluno.selecionar_um(id)
      self.cod_aluno = aluno[0]
      self.nome_var.set(aluno[1])
      self.sexo_var.set(aluno[2])
      self.nascimento_var.set(aluno[3])
    
  def limpar_formulario(self):
    self.nome_var.set('')
    self.sexo_var.set('')
    self.nascimento_var.set('')

  def incluir_aluno(self):
    self.limpar_formulario()
    self.nome_entry.focus_set()

  def excluir_aluno(self, id):
    if(id == ''):
      messagebox.showwarning(title='Alerta', message='Selecione um aluno')
    else:
      values = self.tree.item(id)['values']
      nome = values[0]
      resposta = messagebox.askyesno(title='Confirmação', message=f'Tem certeza que deseja excluir o aluno {nome}?')
      if (resposta):
        Aluno.remover(id)
        messagebox.showinfo(title='Informação', message=f'Aluno {nome} exluído com sucesso!')
        self.tree.delete(id)