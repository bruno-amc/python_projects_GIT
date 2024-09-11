import tkinter as tk
from database import connect_db

def create_list_for_registered_employees():
    conexao = connect_db()
    cursor = conexao.cursor()

    cursor.execute('SELECT * FROM employees')
    list_of_employees = cursor.fetchall()

    conexao.close()
    return list_of_employees

 #FUNÇÃO QUE IRÁ ABRIR UMA JANELA CONTENDO DADOS DE TODOS QUE ESTÃO CADASTRADOS
def window_to_show_registered_employees():
    window_list_employees = tk.Toplevel()
    window_list_employees.title("List with all registers / Lista com o cadastros")

    # Crie um widget de texto para exibir os dados
    texto_dados = tk.Text(window_list_employees)
    texto_dados.pack()

    # Preencha o widget de texto com os dados dos funcionários formatados
    funcionarios = create_list_for_registered_employees()  # Obter a lista de funcionários

    for funcionario in funcionarios:
        id_funcionario, matricula, nome, setor, idade, status = funcionario

        # Converte o status de número para "Ativo" ou "Inativo"
        status_text = "Ativo" if status == 1 else "Inativo"

        # Inserir os dados formatados no widget de texto
        texto_dados.insert(tk.END, f"Matrícula: {matricula}\n")
        texto_dados.insert(tk.END, f"Nome: {nome}\n")
        texto_dados.insert(tk.END, f"Setor: {setor}\n")
        texto_dados.insert(tk.END, f"Idade: {idade}\n")
        texto_dados.insert(tk.END, f"Status: {status_text}\n")
        texto_dados.insert(tk.END, "*"*40 + "\n")  # Separador entre registros

    # Desativar a edição do widget de texto para tornar o conteúdo somente leitura
    texto_dados.config(state=tk.DISABLED)

    # Botão para fechar a janela
    botao_fechar = tk.Button(window_list_employees, text="Fechar", command=window_list_employees.destroy)
    botao_fechar.pack()
