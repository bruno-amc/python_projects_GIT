import tkinter as tk
from tkinter import Toplevel, Label, Entry, Button, StringVar, Text
from database import connect_db

def window_search_register(mensagem_vinda_da_funcao_de_pesquisa=""):
    janela_pesquisar_no_cadastro = Toplevel()
    janela_pesquisar_no_cadastro.title("Pesquisar no cadastro")
    # Widgets na nova janela de cadastro
    rotulo_matricula = Label(janela_pesquisar_no_cadastro, text="Pesquisar por matrícula:")
    entrada_matricula = Entry(janela_pesquisar_no_cadastro)
    resultado_pesquisa = tk.Label(janela_pesquisar_no_cadastro, text="")
    botao_pesquisar = Button(janela_pesquisar_no_cadastro, text="Pesquisar no cadastro",
                           command=lambda: realizar_pesquisa_no_cadastro(entrada_matricula.get(), resultado_pesquisa))

    botao_fechar = Button(janela_pesquisar_no_cadastro, text="Fechar",
                           command=janela_pesquisar_no_cadastro.destroy)
    resultado_pesquisa = tk.Label(janela_pesquisar_no_cadastro, text=f"{mensagem_vinda_da_funcao_de_pesquisa}")
    
    # Organização dos widgets na janela
    rotulo_matricula.pack()
    entrada_matricula.pack()
    resultado_pesquisa.pack()
    botao_pesquisar.pack()
    botao_fechar.pack()


def search_on_database_for_employee_register(matricula):
    conexao = connect_db()
    cursor = conexao.cursor()

    cursor.execute('SELECT * FROM employees WHERE matricula = ?',(matricula,))
    registred_found = cursor.fetchone()

    conexao.close()
    return registred_found


def realizar_pesquisa_no_cadastro(matricula, resultado_pesquisa):
     # Verifica se a matrícula foi encontrada
    register = search_on_database_for_employee_register(matricula)
    
    if register:
        id_funcionario, matricula, nome, setor, idade, status = register
        status_text = "Ativo" if status == 1 else "Inativo"
        mensagem_pesquisa = f"Usuário encontrado.\nMatrícula: {matricula}\nNome: {nome}\nSetor: {setor}\nStatus: {status_text}"
    else:
           mensagem_pesquisa = "Usuário não encontrado"

     # Atualizar o Label com o resultado
    resultado_pesquisa.config(text=mensagem_pesquisa)