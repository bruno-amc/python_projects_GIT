import tkinter as tk
from PIL import Image, ImageTk # biblioteca PILLOW para usar o ícone da lupa com o Tkinter

def create_button_with_image(janela, imagem_path, funcao_clicar):
    # Carregue a imagem usando o Pillow (PIL)
    imagem = Image.open(imagem_path)
    imagem = imagem.resize((32,40))  # redimensionando a imagem

    # Converta a imagem para um formato compatível com o tkinter
    imagem_tk = ImageTk.PhotoImage(imagem)

    # Crie o botão com a imagem como ícone
    botao = tk.Button(janela, image=imagem_tk, command=funcao_clicar)
    botao.imagem = imagem_tk  # Mantendo uma referência à imagem para que o coletor de lixo do python não a limpe
    return botao