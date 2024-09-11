import tkinter as tk
from tkinter import messagebox, ttk
from employees import add_employees
from sectors import list_sectors
from tkinter import messagebox

def open_window_register_new_employees():
    register_window = tk.Toplevel()
    register_window.title("Register new employees.")

     # Função para salvar os dados do cadastro
    def verify_and_save_register():
        matricula = entry_matricula.get()
        nome = entry_nome.get()
        setor_id = combobox_setor.get()  # Pode ser o ID ou o nome do setor
        idade = entry_idade.get()
        status = combobox_status.get()  # Status 1 para ativo e 0 para inativo

         # Verifica se todos os campos estão preenchidos
        if matricula and nome and setor_id and idade and status:
            status_value = 1 if status == "Ativo" else 0
            add_employees(matricula, nome, setor_id, idade, status_value)
            register_window.destroy()  # Fecha a janela após o salvamento
        else:
            # Exibe um erro se algum campo não estiver preenchido
            messagebox.showerror("Erro", "Todos os campos devem ser preenchidos!")

    

    #layout dos campos de cadastro
    tk.Label(register_window, text="Matrícula:").pack()
    entry_matricula = tk.Entry(register_window)
    entry_matricula.pack()

    tk.Label(register_window, text="Nome:").pack()
    entry_nome = tk.Entry(register_window)
    entry_nome.pack()

    tk.Label(register_window, text="Setor:").pack()

    # Listar os setores disponíveis
    setores = list_sectors()
    setores_nomes = [setor[1] for setor in setores]  # Supondo que o segundo item da tupla é o nome do setor
    combobox_setor = tk.ttk.Combobox(register_window, values=setores_nomes)
    combobox_setor.pack()

    tk.Label(register_window, text="Idade:").pack()
    entry_idade = tk.Entry(register_window)
    entry_idade.pack()

    tk.Label(register_window, text="Status:").pack()
    combobox_status = tk.ttk.Combobox(register_window, values=["Ativo", "Inativo"])
    combobox_status.pack()

    # Botão para salvar o cadastro
    tk.Button(register_window, text="Salvar", command=verify_and_save_register).pack()