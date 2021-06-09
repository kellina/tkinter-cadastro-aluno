import tkinter as tk
from tkinter import (ttk, N, E, S, W)
from gui.frame_aluno import FrameAluno
from gui.frame_disciplina import FrameDisciplina
from gui.frame_nota import FrameNota

class NotebookAluno(ttk.Notebook): #classe especializada
  def __init__(self, master=None, **kw):
    super().__init__(master=master, **kw)
    self.place_components()
    
  def place_components(self):
    tabAluno = FrameAluno(self)
    tabDisciplina = FrameDisciplina(self)
    tabNota = FrameNota(self)
    self.add(tabAluno, text='Aluno')
    self.add(tabDisciplina, text='Disciplina')
    self.add(tabNota, text='Nota')
    self.pack(expand=True, fill='both')

