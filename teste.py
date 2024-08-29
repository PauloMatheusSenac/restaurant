# import tkinter as tk

# root = tk.Tk()

# # Exemplo com row, column e sticky
# tk.Label(root, text="Label 1").grid(row=0, column=0, sticky="w", padx=10, pady=10)
# tk.Entry(root).grid(row=0, column=1, sticky="ew", padx=10, pady=10)

# # Exemplo com rowspan e columnspan
# tk.Label(root, text="Label 2").grid(row=1, column=0, columnspan=2, sticky="ew", padx=10, pady=10)
# tk.Button(root, text="Button").grid(row=2, column=1, rowspan=2, padx=10, pady=10)

# # Exemplo com sticky e preenchimento
# tk.Label(root, text="Label 3").grid(row=3, column=0, sticky="nsew", padx=10, pady=10)
# tk.Entry(root).grid(row=3, column=1, sticky="nsew", padx=10, pady=10)

# root.grid_rowconfigure(3, weight=1)  # Configuração para expansão
# root.grid_columnconfigure(1, weight=1)  # Configuração para expansão

# root.mainloop()

import tkinter as tk

def menu(usuario):
    tela_menu = tk.Tk()
    tela_menu.title("Menu")
    tela_menu.geometry("800x800")


    tk_image = tk.PhotoImage(file="C:/Users/PauloSouza/Desktop/Galeria/gato.png")  
    botao_com_imagem = tk.Button(tela_menu, image=tk_image, command=lambda: print("Botão clicado"))
    botao_com_imagem.image = tk_image  
    botao_com_imagem.grid(row=0, column=0, padx=20, pady=20, sticky="nw")




    tela_menu.mainloop()

menu("Usuário")

import tkinter as tk

def menu(usuario):
    tela_menu = tk.Tk()
    tela_menu.title("Menu")
    tela_menu.geometry("800x800")

    # Carregar a imagem PNG ou GIF
    tk_image = tk.PhotoImage(file="caminho/para/sua/imagem.png")  # Substitua pelo caminho da sua imagem

    # Criar o botão com a imagem
    botao_com_imagem = tk.Button(tela_menu, image=tk_image, command=lambda: print("Botão clicado"))
    botao_com_imagem.image = tk_image  # Manter uma referência da imagem para evitar que seja coletada como lixo
    botao_com_imagem.grid(row=0, column=0, padx=20, pady=20, sticky="nw")

    # Adicionar um rótulo de boas-vindas
    menu_label = tk.Label(tela_menu, text=f"Olá {usuario}, SEJA BEM VINDO", font=("Arial", 20))
    menu_label.grid(row=1, column=0, padx=20, pady=20, sticky="nw")

    tela_menu.mainloop()

menu("Usuário")

