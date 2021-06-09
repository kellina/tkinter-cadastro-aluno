import tkinter as tk 
from tkinter import *                   
from tkinter import ttk

class FrameNota(ttk.Frame):
  def __init__(self, master=None, **kw):
    super().__init__(master=master, **kw)
    self.grid(column=0, row=0, sticky=(N, S, E, W))
    Grid.columnconfigure(self, 0, weight=1)
    # Sessão Formulário de cadastro
    form_label_frame = ttk.Labelframe(self, text='Cadastro de Nota')
    #nome e disciplina combobox
    alunos = ('João', 'Maria', 'Ana')
    disciplinas = ('Algoritmos', 'Estrutura de dados', 'Introdução ao python')
    nome_label = tk.Label(form_label_frame, text='Selecione o aluno')
    nome_selecionado = tk.StringVar()
    nome_combo = ttk.Combobox(form_label_frame, textvariable=nome_selecionado)
    nome_combo['values'] = alunos
   
    disciplina_label = tk.Label(form_label_frame, text='Selecione a disciplina')
    disciplina_selecionado = tk.StringVar()
    disciplina_combo = ttk.Combobox(form_label_frame, textvariable=disciplina_selecionado)
    disciplina_combo['values'] = disciplinas
    
    
    nota_label = ttk.Label(form_label_frame, text='Nota:')
    nota_entry = ttk.Entry(form_label_frame)
    btn_salvar = ttk.Button(form_label_frame, text='Salvar')
    
    # Sessão Listagem de disciplinas cadastrados
    listagem_label_frame = ttk.Labelframe(self, text='Relatório do aluno')
    btn_incluir = ttk.Button(listagem_label_frame, text='Incluir')
    btn_alterar = ttk.Button(listagem_label_frame, text='Editar')
    btn_excluir = ttk.Button(listagem_label_frame, text='Excluir')
    
    # Alinhamento dos componentes
    form_label_frame.grid(column=0, row=0, sticky=(E, W), padx=10, pady=10)
    nome_label.grid(column=0, row=0)
    nome_combo.grid(column=1, row=0, pady=5)
    disciplina_label.grid(column=0, row=1)
    disciplina_combo.grid(column=1, row=1, pady=5)
    nota_label.grid(column=0, row=2)
    nota_entry.grid(column=1, row=2, pady=5)
     
    btn_salvar.grid(column=1, row=3, pady=5)
    
    listagem_label_frame.grid(column=0, row=1, sticky=(E, W), pady=10, padx=10)
    
    relatorio = ('João Mateus', 'Algoritmos', '9.5')
    colunas = ('#1', '#2', '#3')
  
    tree = ttk.Treeview(listagem_label_frame, columns=colunas, height=3, show='headings')
    tree.heading('#1', text='Aluno')
    tree.heading('#2', text='Disciplina')
    tree.heading('#3', text='Nota')
    tree.column('#3', anchor='center')
    tree.insert('', 'end', values=relatorio)
    
    tree.grid(column=0, row=0, columnspan=3, padx=(5, 0), pady=5, sticky=(E, W))
    btn_incluir.grid(column=0, row=1, pady=(0, 5))
    btn_alterar.grid(column=1, row=1)
    btn_excluir.grid(column=2, row=1)