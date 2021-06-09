import tkinter as tk 
from tkinter import *                   
from tkinter import ttk

class FrameDisciplina(ttk.Frame):
  def __init__(self, master=None, **kw):
    super().__init__(master=master, **kw)
    self.grid(column=0, row=0, sticky=(N, S, E, W))
    Grid.columnconfigure(self, 0, weight=1)
    # Sessão Formulário de cadastro
    form_label_frame = ttk.Labelframe(self, text='Cadastro de Disciplina')
    nome_label = ttk.Label(form_label_frame, text='Nome:')
    carga_label = ttk.Label(form_label_frame, text='Carga horária:')
    desc_label = ttk.Label(form_label_frame, text='Descrição:')
    nome_entry = ttk.Entry(form_label_frame)
    carga_entry = ttk.Entry(form_label_frame)
    desc_entry = ttk.Entry(form_label_frame)
    btn_salvar = ttk.Button(form_label_frame, text='Salvar')
    
    # Sessão Listagem de disciplinas cadastrados
    listagem_label_frame = ttk.Labelframe(self, text='Disciplinas Cadastrados')
           
    btn_incluir = ttk.Button(listagem_label_frame, text='Incluir')
    btn_alterar = ttk.Button(listagem_label_frame, text='Alterar')
    btn_excluir = ttk.Button(listagem_label_frame, text='Excluir')
    
    
    # Alinhamento dos componentes
    form_label_frame.grid(column=0, row=0, sticky=(E, W), padx=10, pady=10)
    nome_label.grid(column=0, row=0, pady=5, padx=5, sticky=E)
    nome_entry.grid(column=1, row=0, columnspan=2, sticky = (W, E), pady=5)
    carga_label.grid(column=0, row=1, pady=5, padx=5, sticky=E)
    carga_entry.grid(column=1, row=1, columnspan=2, sticky = (W, E), pady=5)
    desc_label.grid(column=0, row=2, padx=5, sticky=E)
    desc_entry.grid(column=1, row=2, columnspan=2, sticky = (W, E), pady=5)
   
    btn_salvar.grid(column=2, row=3, pady=5)
    
    listagem_label_frame.grid(column=0, row=1, sticky=(E, W), pady=10, padx=10)
    
    disciplinas = [
      ('Algoritmos', '40', 'Lorem ipsum, or lipsum as it is sometimes known.'), 
      ('Estrutura de dados', '60', 'Lorem ipsum, or lipsum as it is sometimes known'),
      ('Introdução ao Python', '60', 'Lorem ipsum, or lipsum as it is sometimes known.')
    ]
    colunas = ('#1', '#2', '#3')
    tree = ttk.Treeview(listagem_label_frame, columns=colunas, height=4, show='headings')
    tree.heading('#1', text='Nome')
    tree.heading('#2', text='Carga horária')
    tree.heading('#3', text='Descrição')
    tree.column('#2', anchor='center')
    for disciplina in disciplinas:
      tree.insert('', 'end', values=disciplina)
    
    # Add Scrollbar
    scrollbar = ttk.Scrollbar(listagem_label_frame, orient=VERTICAL, command=tree.yview)
    tree.configure(yscroll=scrollbar.set, height=4)
    
    tree.grid(column=0, row=0, columnspan=3, padx=(5, 0), pady=5, sticky=(E, W))
    scrollbar.grid(column=3, row=0, sticky=(N, S), padx=(0, 5))
    btn_incluir.grid(column=0, row=1, pady=(0, 5))
    btn_alterar.grid(column=1, row=1)
    btn_excluir.grid(column=2, row=1)