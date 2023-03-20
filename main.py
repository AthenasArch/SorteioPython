# from AthenasArch - 19/03/2023 - Leonardo Hilgemberg Lopes
# aprovado por:
#
#
#
#

import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import random
from pathlib import Path
from playsound import playsound

def sortear(nomes, resultado_var):
    print("Acionada Função para realizar o sorteio e exibir o nome sorteado.")
    nome_sorteado = random.choice(nomes)
    resultado_var.set(nome_sorteado)
    
    # Tocar o do vencedor - KKKKKK
    arquivo_som = (Path(__file__).parent / "win.mp3").resolve()
    playsound(arquivo_som, block=False)

def redimensionar_imagem(image, width, height):
    print("Função para redimensionar uma imagem para as dimensões especificadas (A logo).")
    return image.resize((width, height), Image.LANCZOS)

def main():
    # Lista de nomes para o sorteio
    nomes = ["nome_1", "nome_2", "nome_3", "nome_4", "nome_5", "nome_6", "nome_7", "nome_8"]

    # Inicializando a janela principal
    janela = tk.Tk()
    janela.title("Sorteio livro \"Entendendo algoritmos\"")
    janela.geometry("450x450")

    # Alterando o plano de fundo da janela para preto por conta da logo
    janela.configure(bg="black")

    # Adicionando a imagem (logotipo)
    logo_path = "logo.png"  # caminho da imagem do logotipo
    image = Image.open(logo_path)

    # Redimensionando a logo porque é muito grande
    image = redimensionar_imagem(image, 150, 150)

    photo = ImageTk.PhotoImage(image)
    label_logo = ttk.Label(janela, image=photo, background="black")
    label_logo.pack(pady=10)

    # Exibindo o resultado do sorteio
    resultado_var = tk.StringVar()
    resultado_var.set("Nenhum nome sorteado")
    label_resultado = ttk.Label(janela, textvariable=resultado_var, background="black", foreground="white", font=("Arial", 16))
    label_resultado.pack(pady=10)

    # Adicionando o botão de sorteio
    style = ttk.Style()
    style.configure("TButton", background="white", foreground="black")

    # Usando a função lambda para passar a lista de nomes e resultado_var para a função sortear
    botao_sorteio = ttk.Button(janela, text="Sortear", command=lambda: sortear(nomes, resultado_var))
    botao_sorteio.pack(pady=10)

    # Iniciando o loop principal da aplicação
    janela.mainloop()

if __name__ == "__main__":
    main()
