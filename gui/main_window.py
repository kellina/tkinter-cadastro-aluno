import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style
from tkinter import *
from gui.notebook_aluno import NotebookAluno

class MainWindow():
  def show(self):
    root = tk.Tk()

    root.title('FACULDADE DE COMPUTAÇÃO')
    root.geometry('750x450')

    style = Style(theme='journal')

    notebook = NotebookAluno(root)
    app_icone = PhotoImage(file = "gui\\icons\\book.png")
    root.iconphoto(False, app_icone)
    root.mainloop()
