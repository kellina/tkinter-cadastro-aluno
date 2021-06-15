from tkinter import *                   
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from entidades.notas import Nota
from gui.aluno_combo_item import AlunoComboItem
from entidades.aluno import Aluno
from entidades.disciplina import Disciplina
from tkinter.font import Font
class FrameNota(ttk.Frame):
  def __init__(self, master=None, **kw):
    super().__init__(master=master, **kw)
    self.grid(column=0, row=0, sticky=(N, S, E, W))
    Grid.columnconfigure(self, 0, weight=1)
    
    self.aluno_var = StringVar()
    self.disciplina_var = StringVar()
    self.nota1_var = DoubleVar() 
    self.nota2_var = DoubleVar() 
    self.nota3_var = DoubleVar() 
    self.notaD_var = DoubleVar() 
    
    # Sessão Formulário de cadastro
    form_label_frame = ttk.Labelframe(self, text='Cadastro de Nota')
    #nome e disciplina combobox
    
    nome_label = ttk.Label(form_label_frame, text='Selecione o aluno')
    self.nome_combo = ttk.Combobox(form_label_frame, textvariable=self.aluno_var)
    self.popular_alunos_combo()
   
    disciplina_label = ttk.Label(form_label_frame, text='Selecione a disciplina')
    disciplina_selecionado = tk.StringVar()
    self.disciplina_combo = ttk.Combobox(form_label_frame, textvariable=self.disciplina_var)
    self.popular_disciplinas_combo()
        
    nota1_label = ttk.Label(form_label_frame, text='Nota AV1:')
    nota1_entry = ttk.Entry(form_label_frame, textvariable=self.nota1_var)
    nota2_label = ttk.Label(form_label_frame, text='Nota AV2:')
    nota2_entry = ttk.Entry(form_label_frame, textvariable=self.nota2_var)
    nota3_label = ttk.Label(form_label_frame, text='Nota AV3:')
    nota3_entry = ttk.Entry(form_label_frame, textvariable=self.nota3_var)
    notaD_label = ttk.Label(form_label_frame, text='Nota AVD:')
    notaD_entry = ttk.Entry(form_label_frame, textvariable=self.notaD_var)
    btn_salvar = ttk.Button(form_label_frame, text='Salvar', command=lambda: self.salvar_notas())
    
    # Sessão Listagem de disciplinas cadastrados
    listagem_label_frame = ttk.Labelframe(self, text='Relatório do aluno')
    btn_incluir = ttk.Button(listagem_label_frame, text='Incluir',
                             command=lambda: self.incluir_notas())
    btn_alterar = ttk.Button(listagem_label_frame, text='Editar',
                             command=lambda: self.alterar_notas(self.tree.focus()))
    btn_excluir = ttk.Button(listagem_label_frame, text='Excluir',
                             command=lambda: self.excluir_notas(self.tree.focus()))
    
    # Alinhamento dos componentes
    form_label_frame.grid(column=0, row=0, sticky=(E, W), padx=10, pady=10)
    nome_label.grid(column=0, row=0)
    self.nome_combo.grid(column=1, row=0, pady=5)
    disciplina_label.grid(column=0, row=1)
    self.disciplina_combo.grid(column=1, row=1, pady=5)
    nota1_label.grid(column=2, row=0, padx=(10, 0))
    nota1_entry.grid(column=3, row=0, pady=5)
    nota2_label.grid(column=2, row=1, padx=(10, 0))
    nota2_entry.grid(column=3, row=1, pady=5)
    nota3_label.grid(column=2, row=2, padx=(10, 0))
    nota3_entry.grid(column=3, row=2, pady=5)
    notaD_label.grid(column=2, row=3, padx=(10, 0))
    notaD_entry.grid(column=3, row=3, pady=5)
     
    btn_salvar.grid(column=4, row=3, padx=10)
    
    listagem_label_frame.grid(column=0, row=1, sticky=(E, W), pady=10, padx=10)
    
    colunas = ('#1', '#2', '#3', '#4', '#5', '#6', '#7', '#8')
    self.tree = ttk.Treeview(listagem_label_frame, columns=colunas, height=3, show='headings')
    self.tree.heading('#1', text='Aluno')
    self.tree.column('#1', minwidth=0, width=150)
    self.tree.heading('#2', text='Disciplina')
    self.tree.column('#2', minwidth=0, width=150)
    self.tree.heading('#3', text='AV1')
    self.tree.column('#3', anchor='center', minwidth=0, width=50, stretch=NO)
    self.tree.heading('#4', text='AV2')
    self.tree.column('#4', anchor='center', minwidth=0, width=50, stretch=NO)
    self.tree.heading('#5', text='AVD')
    self.tree.column('#5', anchor='center', minwidth=0, width=50, stretch=NO)
    self.tree.heading('#6', text='AV3')
    self.tree.column('#6', anchor='center', minwidth=0, width=50, stretch=NO)
    self.tree.heading('#7', text='Média')
    self.tree.column('#7', anchor='center', minwidth=0, width=50, stretch=NO)
    self.tree.heading('#8', text='Situação')
    self.tree.column('#8', anchor='center', minwidth=0, width=100, stretch=NO)
    self.popular_tree()
    
    # Add Scrollbar
    scrollbar = ttk.Scrollbar(listagem_label_frame, orient=VERTICAL, command=self.tree.yview)
    self.tree.configure(yscroll=scrollbar.set, height=4)
    
    self.tree.grid(column=0, row=0, columnspan=4, padx=(5, 0), pady=5, sticky=(E, W))
    scrollbar.grid(column=8, row=0, sticky=(N, S), padx=(0, 5))
    btn_incluir.grid(column=0, row=1, pady=(0, 5))
    btn_alterar.grid(column=1, row=1)
    btn_excluir.grid(column=2, row=1)
  
    # Configurando a tag
    self.tree.tag_configure('blue', foreground='blue')
    self.tree.tag_configure('red', foreground='red')
    
  @staticmethod
  def tree_map(nota):
    nota_av1 = nota[2]
    nota_av2 = nota[3]
    nota_avd = nota[4]
    nota_av3 = nota[5]
    nome_aluno = nota[6]
    nome_disciplina = nota[7]
    media = nota[8]
    return (
      nome_aluno, nome_disciplina,
      nota_av1, nota_av2, nota_avd, nota_av3, media,
      "Aprovado" if media >= 6.0 else "Reprovado"
    )
    
  def popular_tree(self):
    notas = Nota.selecionar_todas_notas()
    notas_tree = list(map(FrameNota.tree_map, notas))
    self.limpar_tree()
    for key, nota in enumerate(notas):
      media = nota[8]
      if media >= 6.0:
        self.tree.insert('', index='end', iid=f'{nota[0]}:{nota[1]}', values=notas_tree[key], tags=['blue']) 
      else:
        self.tree.insert('', index='end', iid=f'{nota[0]}:{nota[1]}', values=notas_tree[key], tags=['red'])

  def limpar_tree(self):
    for i in self.tree.get_children():
      self.tree.delete(i)
  
  def limpar_formulario(self):
    self.nota1_var.set('')
    self.nota2_var.set('')
    self.nota3_var.set('')
    self.notaD_var.set('')
  
  def extrairId(self, desc):
    return int(desc.split("-")[0].strip())
  
  def salvar_notas(self):
    print('Salvando notas')
    nota = Nota(
      self.extrairId(self.aluno_var.get()),
      self.extrairId(self.disciplina_var.get()),
      self.nota1_var.get(),
      self.nota2_var.get(),
      self.nota3_var.get(),
      self.notaD_var.get()
    )
    nota.inserir()
    self.limpar_formulario()
    self.popular_tree()
    
  def incluir_notas(self):
    print('Incluindo notas')
    self.limpar_formulario()
    self.nome_combo.focus_set()
  
  def alterar_notas(self, id):
    print('Alterando notas')
    if(id == ''):
      messagebox.showwarning(title='Alerta', message='Selecione uma nota de um aluno em alguma disciplina')
    else:
      cod_aluno = int(id.split(":")[0])
      cod_disciplina = int(id.split(":")[1])
      nota = Nota.selecionar_nota_aluno_disciplina(cod_aluno, cod_disciplina)
      self.aluno_var.set(f"{nota[0]} - {nota[6]}")
      self.disciplina_var.set(f"{nota[1]} - {nota[7]}")
      self.nota1_var.set(nota[2])
      self.nota2_var.set(nota[3])
      self.nota3_var.set(nota[4])
      self.notaD_var.set(nota[5])
  
  def excluir_notas(self, id):
    print('Excluindo notas')
    if(id == ''):
      messagebox.showwarning(title='Alerta', message='Selecione um aluno em alguma disciplina')
    else:
      cod_aluno = int(id.split(":")[0])
      cod_disciplina = int(id.split(":")[1])
      nota = Nota.selecionar_nota_aluno_disciplina(cod_aluno, cod_disciplina)
      values = self.tree.item(id)['values']     
      resposta = messagebox.askyesno(title='Confirmação', message=f'Tem certeza que deseja excluir a nota?')
      if (resposta):
        Nota.remover_nota(cod_aluno, cod_disciplina)
        messagebox.showinfo(title='Informação', message=f'Nota exluída com sucesso!')
        self.tree.delete(*cod_aluno, *cod_disciplina)
        
    
  def popular_alunos_combo(self):
    alunos_combo = []
    for aluno in Aluno.selecionar_todos():
      alunos_combo.append(AlunoComboItem(aluno[0], aluno[1]))
    self.nome_combo['values'] = alunos_combo
  
  def popular_disciplinas_combo(self):
    disciplinas_combo = []
    for disciplina in Disciplina.selecionar_todas():
      disciplinas_combo.append(AlunoComboItem(disciplina[0], disciplina[1]))
    self.disciplina_combo['values'] = disciplinas_combo
  