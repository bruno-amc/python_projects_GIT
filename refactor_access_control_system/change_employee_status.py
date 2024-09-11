import tkinter as tk
from employees import add_employees
from sectors import list_sectors
from tkinter import messagebox
from database import connect_db
from tkinter import Toplevel, Label, Entry, Button, StringVar, Text



def window_for_changing_employee_status():
    window_change_status = Toplevel()
    window_change_status.title("Ativar ou Inativar Usuários")

    rotulo_matricula_status = tk.Label(window_change_status, text="Insirir matrícula para alterar o status:\n")
    entrada_matricula_status = Entry(window_change_status)
    botao_pesquisar_matricula_status = Button(window_change_status, text="Pesquisar status no cadastro",
                           command=lambda: mostrar_label_ao_pesquisar_status(
                                                                        entrada_matricula_status.get(), 
                                                                        resultado_status))
    botao_alterar_status = Button(window_change_status, text="Clique Para Alterar o Status\n do Usuário",
                           command= lambda: realizar_alteracao_status(  entrada_matricula_status.get(),
                                                                        resultado_status_apos_a_alteracao,resultado_status
                                                                        ))
      
    
    botao_fechar = Button(window_change_status, text="Fechar",
                          command=window_change_status.destroy)

    resultado_status = tk.Label(window_change_status, text="")
    resultado_status_apos_a_alteracao = tk.Label(window_change_status, text="")

    botao_limpar_campos = Button(window_change_status, text="Limpar os campos",
                                   command= lambda: limpar_campos_mudanca_status(resultado_status,
                                                                                 resultado_status_apos_a_alteracao, entrada_matricula_status)
              )
    
    # Organização dos widgets na janela
    rotulo_matricula_status.pack()
    entrada_matricula_status.pack()
    botao_pesquisar_matricula_status.pack()
    resultado_status.pack()
    botao_alterar_status.pack()
    resultado_status_apos_a_alteracao.pack()
    botao_limpar_campos.pack()
    botao_fechar.pack()


def buscar_status_no_banco(matricula):
    conexao = connect_db()
    cursor = conexao.cursor()
    cursor.execute('SELECT status FROM employees WHERE matricula = ?', (matricula,))
    status = cursor.fetchone()  # Pode retornar None, ou a tupla (1,) ou (0,)
    conexao.close()
    return status[0] if status else None #[0] >> pega a primeira posição da tupla, 0 ou 1.

def mostrar_label_ao_pesquisar_status(matricula, resultado_status):
 
    status = buscar_status_no_banco(matricula)
    status_text = "Ativo" if status == 1 else "Inativo"

    if status is not None:
        situacao = f"Register Nº {matricula} is {status_text}"
    else:
        situacao = "Status/User not found"
    resultado_status.config(text=f"{situacao}")



def realizar_alteracao_status(matricula, resultado_status_apos_a_alteracao,resultado_status):
    try:
        conexao = connect_db()
        cursor = conexao.cursor()


        ##  using CASE (similar to IF/ELSE) to change between 1 and 0

        cursor.execute('''UPDATE employees SET status = CASE
                    WHEN status = 0 THEN 1 
                        ELSE 0
                        END
                    WHERE matricula = ?''',(matricula,))
        conexao.commit()

        # searching the new status and using a variable to store it
        cursor.execute('SELECT status FROM employees WHERE matricula = ?', (matricula,))
        status = cursor.fetchone()[0]  # first item of the tuple
        conexao.close()

        status_text = "Ativo" if status == 1 else "Inativo"
        resultado_status_apos_a_alteracao.config(text="New status: "+status_text)
        resultado_status.config(text=f"")

    except Exception as e:
        resultado_status_apos_a_alteracao.config(text=f"Error: {e}")


def limpar_campos_mudanca_status(result1, result2, entrada_matricula_status):
    result1.config(text=" ")
    result2.config(text=" ")
    entrada_matricula_status.delete(0, tk.END)