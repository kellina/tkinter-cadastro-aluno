import tkinter as tk
from tkinter import messagebox
from database_notas import Database

db = Database('alunos.db')


def add_item():
    if nome_txt.get() == '' or sexo_txt.get() == '' or nascimento_txt.get() == '' or curso_txt.get() == '':
        messagebox.showerror('Campos Obrigatórios',
                             'Por favor, preencha todos os campos')
        return
    db.insert(nome_txt.get(), sexo_txt.get(),
              nascimento_txt.get(), curso_txt.get())
    messagebox.showinfo('Confirmação', 'Aluno cadastrado com sucesso!')
    clear_text()


def clear_text():
    nome_txt.delete(0, 'end')
    sexo_txt.delete(0, 'end')
    nascimento_txt.delete(0, 'end')
    curso_txt.delete(0, 'end')


root = tk.Tk()

root.title('CADASTRO DE ALUNOS')
root.geometry('645x270')
root.configure(background='#dde')

nome_label = tk.Label(
    root, text='Nome:', background='#dde', foreground='#009', anchor='w')
nome_label.place(x=30, y=20, width=200, height=30)

nome_txt = tk.Entry(root)
nome_txt.place(x=30, y=48, width=270, height=30)
nome_txt.focus()

sexo_label = tk.Label(
    root, text='Sexo:', background='#dde', foreground='#009', anchor='w')
sexo_label.place(x=30, y=90, width=200, height=30)

sexo_txt = tk.Entry(root)
sexo_txt.place(x=30, y=118, width=270, height=30)

curso_label = tk.Label(
    root, text='Nascimento:', background='#dde', foreground='#009', anchor='w')
curso_label.place(x=330, y=20, width=200, height=30)

curso_txt = tk.Entry(root)
curso_txt.place(x=330, y=48, width=280, height=30)

nascimento_label = tk.Label(
    root, text='Curso:', background='#dde', foreground='#009', anchor='w')
nascimento_label.place(x=330, y=90, width=200, height=30)

nascimento_txt = tk.Entry(root)
nascimento_txt.place(x=330, y=118, width=130, height=30)

# Botões
add_btn = tk.Button(root, text='Cadastrar Aluno', command=add_item)
add_btn.place(x=10, y=180, width=100, height=30)

select_btn = tk.Button(root, text='Listar Alunos', command=add_item)
select_btn.place(x=120, y=180, width=100, height=30)

update_btn = tk.Button(root, text='Atualizar Aluno', command=add_item)
update_btn.place(x=230, y=180, width=100, height=30)

del_btn = tk.Button(root, text='Excluir Aluno', command=add_item)
del_btn.place(x=340, y=180, width=100, height=30)

clear_btn = tk.Button(root, text='Limpar Campos', command=clear_text)
clear_btn.place(x=500, y=120, width=100, height=30)
# Start program
root.mainloop()