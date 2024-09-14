import tkinter as tk
from tkinter import Label, Button
from button_with_image import create_button_with_image
from database import creat_tables
from register import open_window_register_new_employees
from show_registered_employees import window_to_show_registered_employees
from search_registered_employee import window_search_register
from change_employee_status import window_for_changing_employee_status
from access_control import process_register_number
from sectors import botao_gerenciar_setores_main

def init_aplication():
    creat_tables() #create tables when the aplication is started

    window = tk.Tk()
    window.title("Access Control - Controle de Acessos")
    icon = "assets/catraca.ico"  # arquivo na extensão .ico que está no mesmo diretório do programa
    window.iconbitmap(icon)
    # Criação do botão de pesquisar com o desenho da lupa e do botão de ativar/inativar usuários
    botao_lupa_pesquisar = create_button_with_image(window, "assets/lupa.png", window_search_register) #janela_para_pesquisar_no_cadastro
    botao_inativar_ativar_usuario = create_button_with_image(window, "assets/inativarAtivarUsuario.png", window_for_changing_employee_status) #janela_para_alterar_status
    rotulo_botao_lupa_pesquisar = tk.Label(window, text="Pesquisar no cadastro:")
    rotulo_botao_ativar_inativar = tk.Label(window, text="Ativar/Inativar usuário")

    #layout and buttons
    collaborator_label = tk.Label(window, text="Colaborator: ")
    input_collaborator = tk.Entry(window)
    espaco = Label(window, text="", width=10, height=2) # space / espaço em branco para afastar o botão do campo de input
    botao_novos_usuarios = Button(window, text="Cadastrar Nova Pessoa",command=open_window_register_new_employees )
    resultado = tk.Label(window, text="")
    botao_lista_usuarios_cadastrados = Button(window, text="Exibir usuários cadastrados", command=window_to_show_registered_employees )
    botao_gerenciar_setores = Button(window, text="Gerenciar Setores", command=botao_gerenciar_setores_main )#command=janela_para_exibir_lista_cadastros

    resultado2 = tk.Label(window, text="")
    

     # Função que processa o número ao pressionar Enter
    def process_register_number_with_input(event=None):
        numero = input_collaborator.get()  # Captura o valor inserido no campo de entrada
        process_register_number(numero, resultado, input_collaborator )  # Chama a função com o valor capturado


    # Associa o evento de tecla pressionada (Enter) à função de processamento
    input_collaborator.bind('<Return>', process_register_number_with_input)
    # Layout
    collaborator_label.pack()
    input_collaborator.pack()
    resultado.pack()
    espaco.pack()
    botao_novos_usuarios.pack()
    botao_lista_usuarios_cadastrados.pack()
    rotulo_botao_lupa_pesquisar.pack()
    botao_lupa_pesquisar.pack() # botão da lupa para pesquisar no cadastro
    rotulo_botao_ativar_inativar.pack()
    botao_inativar_ativar_usuario.pack() # botão para mudar status dos usuarios
    botao_gerenciar_setores.pack() # botão para gerenciar os setores cadastrados
    resultado2.pack()

    window.mainloop()

if __name__ == "__main__":
    init_aplication()