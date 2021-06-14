from tkinter import *                   
from tkinter import ttk
from tkinter import messagebox
from entidades.disciplina import Disciplina

class FrameDisciplina(ttk.Frame):
  def __init__(self, master=None, **kw):
    super().__init__(master=master, **kw)
    self.grid(column=0, row=0, sticky=(N, S, E, W))
    Grid.columnconfigure(self, 0, weight=1)
    # Sessão Formulário de cadastro
    self.cod_disciplina = None
    self.nome_var = StringVar()
    self.carga_var = StringVar()
    self.descricao_var = StringVar()
    
    form_label_frame = ttk.Labelframe(self, text='Cadastro de Disciplina')
    nome_label = ttk.Label(form_label_frame, text='Nome:')
    carga_label = ttk.Label(form_label_frame, text='Carga horária:')
    desc_label = ttk.Label(form_label_frame, text='Descrição:')
    
    self.nome_entry = ttk.Entry(form_label_frame, textvariable=self.nome_var)
    carga_entry = ttk.Entry(form_label_frame, textvariable=self.carga_var)
    desc_entry = ttk.Entry(form_label_frame, textvariable=self.descricao_var)
    btn_salvar = ttk.Button(form_label_frame, text='Salvar', command=lambda: self.salvar_disciplina())
    
    # Sessão Listagem de disciplinas cadastrados
    listagem_label_frame = ttk.Labelframe(self, text='Disciplinas Cadastrados')
           
    btn_incluir = ttk.Button(listagem_label_frame, text='Incluir',
                             command=lambda: self.incluir_disciplina())
    btn_alterar = ttk.Button(listagem_label_frame, text='Alterar',
                             command=lambda: self.alterar_disciplina(self.tree.focus()))
    btn_excluir = ttk.Button(listagem_label_frame, text='Excluir', 
                             command=lambda: self.excluir_disciplina(self.tree.focus()))
    
    
    # Alinhamento dos componentes
    form_label_frame.grid(column=0, row=0, sticky=(E, W), padx=10, pady=10)
    nome_label.grid(column=0, row=0, pady=5, padx=5, sticky=E)
    self.nome_entry.grid(column=1, row=0, columnspan=2, sticky = (W, E), pady=5)
    carga_label.grid(column=0, row=1, pady=5, padx=5, sticky=E)
    carga_entry.grid(column=1, row=1, columnspan=2, sticky = (W, E), pady=5)
    desc_label.grid(column=0, row=2, padx=5, sticky=E)
    desc_entry.grid(column=1, row=2, columnspan=2, sticky = (W, E), pady=5)
   
    btn_salvar.grid(column=2, row=3, pady=5)
    
    listagem_label_frame.grid(column=0, row=1, sticky=(E, W), pady=10, padx=10)
    
    colunas = ('#1', '#2', '#3')
    self.tree = ttk.Treeview(listagem_label_frame, columns=colunas, height=4, show='headings')
    self.tree.heading('#1', text='Nome')
    self.tree.heading('#2', text='Carga horária')
    self.tree.heading('#3', text='Descrição')
    self.tree.column('#2', anchor='center')
    
    self.popular_tree()   

    # Add Scrollbar
    scrollbar = ttk.Scrollbar(listagem_label_frame, orient=VERTICAL, command=self.tree.yview)
    self.tree.configure(yscroll=scrollbar.set, height=4)
    
    self.tree.grid(column=0, row=0, columnspan=3, padx=(5, 0), pady=5, sticky=(E, W))
    scrollbar.grid(column=3, row=0, sticky=(N, S), padx=(0, 5))
    btn_incluir.grid(column=0, row=1, pady=(0, 5))
    btn_alterar.grid(column=1, row=1)
    btn_excluir.grid(column=2, row=1)

  # Funções para fazer o bind
  def popular_tree(self):
    disciplinas = Disciplina.selecionar_todas()
    self.limpar_tree()
    for disciplina in disciplinas:
      disciplina = list(disciplina)
      self.tree.insert('', index='end', iid=disciplina[0], values=disciplina[1:])
      
  def limpar_tree(self):
    for i in self.tree.get_children():
      self.tree.delete(i)
      
  def salvar_disciplina(self):
    disciplina = Disciplina(self.nome_var.get(), self.carga_var.get(), self.descricao_var.get())
    if(self.cod_disciplina == None):
      disciplina.inserir()
      messagebox.showinfo(title='Informação', message=f'Disciplina {self.nome_var.get()} inserida com sucesso!')
    else:
      disciplina.cod_disciplina = self.cod_disciplina
      disciplina.atualizar()
      messagebox.showinfo(title='Informação', message=f'Disciplina {self.nome_var.get()} alterada com sucesso!') 
    self.limpar_formulario()
    self.popular_tree()
    
  def alterar_disciplina(self, id):
    if(id == ''):
      messagebox.showwarning(title='Alerta', message='Selecione uma disciplina')
    else:
      disciplina = Disciplina.selecionar_uma(id)
      self.cod_disciplina = disciplina[0]
      self.nome_var.set(disciplina[1])
      self.carga_var.set(disciplina[2])
      self.descricao_var.set(disciplina[3])
  
  def limpar_formulario(self):
    self.nome_var.set('')
    self.carga_var.set('')
    self.descricao_var.set('')
    
  def incluir_disciplina(self):
    self.limpar_formulario()
    self.nome_entry.focus_set()
      
  def excluir_disciplina(self, id):
    if(id == ''):
      messagebox.showwarning(title='Alerta', message='Selecione uma disciplina')
    else:
      values = self.tree.item(id)['values']
      nome = values[0]
      resposta = messagebox.askyesno(title='Confirmação', message=f'Tem certeza que deseja excluir a disciplina {nome}?')
      if (resposta):
        Disciplina.remover(id)
        messagebox.showinfo(title='Informação', message=f'Disciplina {nome} exluída com sucesso!')
        self.tree.delete(id)
        