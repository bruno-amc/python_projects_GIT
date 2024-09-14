import tkinter as tk
from tkinter import Button, Entry, Label, Toplevel
from database import connect_db

def add_sector(sector,resultado):
    conexao = connect_db()
    cursor = conexao.cursor()

    #check if the sector already exists
    cursor.execute('SELECT * FROM sectors WHERE sector = ?',(sector,))
    setor_existente = cursor.fetchone()

    if setor_existente:
        # verify if the sector already exists, if so, shows a message
        resultado.config(text="Erro: Setor já existe!")

    else:
        # if it doesn't exists >> insert a new sector
        cursor.execute('INSERT INTO sectors (sector) VALUES (?)', (sector,))
        conexao.commit()
        resultado.config(text="Setor adicionado com sucesso!")
    conexao.close()

def list_sectors(): 
    conexao = connect_db()
    cursor = conexao.cursor()

    cursor.execute('SELECT * FROM sectors')
    list_of_sectors = cursor.fetchall()

    conexao.close()
    return list_of_sectors


def remove_sector(setor, resultado): 
    conexao = connect_db()
    cursor = conexao.cursor()

    # Verifica se algum funcionário está associado a esse setor
    cursor.execute('SELECT COUNT(*) FROM employees WHERE setor_id = ?', (setor,))
    funcionarios_no_setor = cursor.fetchone()[0]
    

    if funcionarios_no_setor > 0:
        print(f"Erro: Não é possível remover o setor. Existem {funcionarios_no_setor} funcionários associados a ele.")
        resultado.config(text=f"Erro: Não é possível remover o setor. Existem {funcionarios_no_setor} funcionários associados a ele.")
    else:
        # Remove o setor se não houver funcionários associados
        #antes de remover, vamos verificar se o setor existe
    
        cursor.execute('SELECT * FROM sectors WHERE sector = ?',(setor,))
        setor_existente = cursor.fetchone()

        if setor_existente:
        # verify if the sector already exists, if so, shows a message
            cursor.execute('DELETE FROM sectors WHERE sector = ?', (setor,))
            conexao.commit()
            resultado.config(text=f"Sector '{setor}' removed!")
        else:
            resultado.config(text="Error: Sector doesn't exists!")
    conexao.close()


def edit_sector(id, new_name): #não usado ainda
    conexao = connect_db()
    cursor = conexao.cursor()

    cursor.execute('UPDATE sectors SET sector = ? WHERE id = ?', (new_name, id))
    conexao.commit()
    conexao.close()

    print(f"Setor com id {id} foi atualizado para {new_name}.")


def list_employees_by_sector(setor_id): #não usado ainda
    conexao = connect_db()
    cursor = conexao.cursor()

    cursor.execute('SELECT * FROM employees WHERE setor_id = ?', (setor_id,))
    employees = cursor.fetchall()

    conexao.close()
    return employees

## CÓDIGO ABAIXO REFERENTE AO BOTÃO DE GERENCIAR SETORES DA APLICAÇÃO / CODE FOR THE MANAGE SECTORS BUTTON FROM THE MAIN.PY  ##

def botao_gerenciar_setores_main():
    janela_gerenciar_setores = Toplevel()
    janela_gerenciar_setores.title("Sectors Management / Gerenciamento de setores")
    # Widgets na nova janela de cadastro
    
    botao_add_sectors = Button(janela_gerenciar_setores, text="Add Sectors",
                           command=window_add_sector )
    botao_list_sectors = Button(janela_gerenciar_setores, text="List All Sectors",
                           command=window_list_sector)
    botao_remove_sectors = Button(janela_gerenciar_setores, text="Remove Sectors",
                           command=window_remove_sector)
    botao_edit_sectors = Button(janela_gerenciar_setores, text="Edit Sectors",
                           command=pular)
    botao_list_employees_by_sectors = Button(janela_gerenciar_setores, text="List Employees By Sector",
                           command=pular)

    botao_fechar = Button(janela_gerenciar_setores, text="Fechar",
                           command=janela_gerenciar_setores.destroy)
    
    # Organização dos widgets na janela
   
    botao_add_sectors.pack()
    botao_list_sectors.pack()
    botao_remove_sectors.pack()
    botao_edit_sectors.pack()
    botao_list_employees_by_sectors.pack()
    botao_fechar.pack()

def window_add_sector():
    window_add_sector = Toplevel()
    window_add_sector.title("Add Sector")


    botao_add_sector = Button(window_add_sector, text="Add Sector",
                           command=lambda: add_sector(input_sector.get(), resultado) )
    
    botao_fechar = Button(window_add_sector, text="Fechar",
                           command=window_add_sector.destroy)
    input_sector = tk.Entry(window_add_sector)

    espaco = Label(window_add_sector, text="", width=10, height=2) # space
    resultado = tk.Label(window_add_sector, text="")

    espaco.pack()
    input_sector.pack()
    espaco.pack()
    botao_add_sector.pack()
    resultado.pack()
    botao_fechar.pack()
    


def window_list_sector():
    window_list_sector = Toplevel()
    window_list_sector.title("List of Sectors")
    texto_dados = tk.Text(window_list_sector)
    texto_dados.pack()

    list_of_all_sectors = list_sectors()

    if list_of_all_sectors:  # Verifica se há setores no banco de dados
        for _, sector_name in list_of_all_sectors: #usamos o "_" para indicar que não será usado o ID dos setores
            texto_dados.insert(tk.END, f"{sector_name}\n")
    else:
        # Se não houver setores, exibe uma mensagem informando isso
        texto_dados.insert(tk.END, "Nenhum setor cadastrado.\n")

     # Desativar a edição do widget de texto para tornar o conteúdo somente leitura
    texto_dados.config(state=tk.DISABLED)
    # Botão para fechar a janela
    botao_fechar = tk.Button(window_list_sector, text="Fechar", command=window_list_sector.destroy)
    botao_fechar.pack()

    




def window_remove_sector():
    window_remove_sector = Toplevel()
    window_remove_sector.title("Remove Sector")

    rotulo_remove_sector = tk.Label(window_remove_sector, text="Sector to be removed:")
    botao_remove_sector = Button(window_remove_sector, text="Remove Sector",
                           command=lambda: remove_sector(input_sector.get(), resultado) )
    
    botao_fechar = Button(window_remove_sector, text="Fechar",
                           command=window_remove_sector.destroy)
    input_sector = tk.Entry(window_remove_sector)

    espaco = Label(window_remove_sector, text="", width=10, height=2) # space
    resultado = tk.Label(window_remove_sector, text="")

    espaco.pack()
    rotulo_remove_sector.pack()
    input_sector.pack()
    espaco.pack()
    botao_remove_sector.pack()
    resultado.pack()
    botao_fechar.pack() 


def pular():
    pass


