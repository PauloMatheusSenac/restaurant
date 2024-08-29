import tkinter as tk
from tkinter import messagebox

class Sistema:
    def __init__(self):
        self.logins = {"admin": "123"}
        self.pedidos = []  
        self.inicio()

    def inicio(self):
        self.inicial = tk.Tk()
        self.inicial.title("Escolhe")
        self.inicial.geometry("1x1")
        escolha = messagebox.askyesno(title="Logar ou Cadastrar", message="Você já tem cadastro em nosso sistema?")
        self.inicial.destroy()
        self.window = tk.Tk()
        self.window.title("Login")

        if escolha:
            self.login()
        else:
            self.cadastrar()

        self.window.mainloop()

    def login(self):
        tk.Label(self.window, text="Usuário:").grid(row=0, column=0, padx=10, pady=10)
        self.caixa_usuario = tk.Entry(self.window)
        self.caixa_usuario.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(self.window, text="Senha:").grid(row=1, column=0, padx=10, pady=10)
        self.caixa_senha = tk.Entry(self.window, show='*')
        self.caixa_senha.grid(row=1, column=1, padx=10, pady=10)

        tk.Button(self.window, text="Login", command=self.logar).grid(row=2, column=1, pady=20, padx=50)

    def cadastrar(self):
        tk.Label(self.window, text="Usuário:").grid(row=0, column=0, padx=10, pady=10)
        self.caixa_usuario = tk.Entry(self.window)
        self.caixa_usuario.grid(row=0, column=1, columnspan=2, padx=10, pady=10)

        tk.Label(self.window, text="Senha:").grid(row=1, column=0, padx=10, pady=10)
        self.caixa_senha = tk.Entry(self.window, show='*')
        self.caixa_senha.grid(row=1, column=1, columnspan=2, padx=10, pady=10)

        tk.Label(self.window, text="Confirmação de Senha:").grid(row=2, column=0, padx=10, pady=10)
        self.caixa_conf_senha = tk.Entry(self.window, show='*')
        self.caixa_conf_senha.grid(row=2, column=1, columnspan=2, padx=10, pady=10)

        tk.Button(self.window, text="Cadastrar", command=self.incluir).grid(row=3, column=1, pady=20, padx=20)

    def logar(self):
        usuario = self.caixa_usuario.get()
        senha = self.caixa_senha.get()

        if usuario and senha:
            if usuario in self.logins:
                if senha == self.logins[usuario]:
                    messagebox.showinfo("Login bem-sucedido", f"Olá {usuario}, Seja Bem Vindo!")
                    self.window.destroy()
                    self.menu(usuario)
                else:
                    messagebox.showwarning("Senha", "Senha Incorreta")
            else:
                messagebox.showwarning("Não encontrado", "Usuário não cadastrado!")
        else:
            messagebox.showwarning("Aviso", "Campo Não preenchido, confira os campos e tente novamente!")

    def incluir(self):
        usuario = self.caixa_usuario.get()
        senha = self.caixa_senha.get()
        conf_senha = self.caixa_conf_senha.get()

        if usuario and senha and conf_senha:
            if senha != conf_senha:
                messagebox.showwarning("Senha", "Senhas não coincidem!")
            elif usuario == senha:
                messagebox.showwarning("Erro", "Usuário e senha não podem coincidir!")
            else:
                self.logins[usuario] = senha
                messagebox.showinfo("Cadastro", "Cadastro Realizado com Sucesso!")
                pedido = messagebox.askyesno("Pedido", "Deseja fazer seu pedido?")
                if pedido:
                    self.window.destroy()
                    self.menu(usuario)
                else:
                    self.window.destroy()
        else:
            messagebox.showwarning("Aviso", "Campo Não preenchido, confira os campos e tente novamente!")

    def menu(self, usuario):
        self.menu_window = tk.Tk()
        self.menu_window.title("Menu")
        self.menu_window.geometry("400x800")

        menu_label = tk.Label(self.menu_window, text=f"Olá {usuario}, SEJA BEM VINDO", font=("Arial", 20))
        menu_label.grid(row=0, column=0, sticky="nw", padx=20, pady=20)

        tk_principal = tk.PhotoImage(file="C:/Users/PauloSouza/Desktop/Restaurante/pratos_principais.png").subsample(5, 5)
        tk_bebidas = tk.PhotoImage(file="C:/Users/PauloSouza/Desktop/Restaurante/bebidas.png").subsample(5, 5)
        tk_alcoolicas = tk.PhotoImage(file="C:/Users/PauloSouza/Desktop/Restaurante/bebidas_alcoólicas.png").subsample(5, 5)
        tk_sobremesas = tk.PhotoImage(file="C:/Users/PauloSouza/Desktop/Restaurante/sobremesas.png").subsample(5, 5)
        tk_menu_chef = tk.PhotoImage(file="C:/Users/PauloSouza/Desktop/Restaurante/menu_do_chef.png").subsample(5, 5)
        tk_entradas = tk.PhotoImage(file="C:/Users/PauloSouza/Desktop/Restaurante/entradas.png").subsample(5, 5)
        tk_pedidos = tk.PhotoImage(file="C:/Users/PauloSouza/Desktop/Restaurante/pedir.png").subsample(5, 5)

        botao_entradas = tk.Button(self.menu_window, image=tk_entradas, command=lambda: self.categorias("entradas"))
        botao_entradas.grid(row=1, column=0, pady=20, padx=50, sticky="nw") 
        desc_entradas = tk.Label(self.menu_window, text="ENTRADAS", font=("Arial", 10))
        desc_entradas.grid(row=2, column=0, sticky="nw", padx=65)

        botao_principal = tk.Button(self.menu_window, image=tk_principal, command=lambda: self.categorias("pratos"))
        botao_principal.grid(row=3, column=0, pady=20, padx=50, sticky="nw")
        desc_principal = tk.Label(self.menu_window, text="PRATOS PRINCIPAIS", font=("Arial", 10))
        desc_principal.grid(row=4, column=0, sticky="nw", padx=40)

        botao_bebidas = tk.Button(self.menu_window, image=tk_bebidas, command=lambda: self.categorias("bebidas"))
        botao_bebidas.grid(row=5, column=0, pady=20, padx=50, sticky="nw")
        desc_bebidas = tk.Label(self.menu_window, text="BEBIDAS", font=("Arial", 10))
        desc_bebidas.grid(row=6, column=0, sticky="nw", padx=65)

        botao_alcoolicas = tk.Button(self.menu_window, image=tk_alcoolicas, command=lambda: self.categorias("alcoolicas"))
        botao_alcoolicas.grid(row=1, column=0, pady=20, padx=50, sticky="ne")
        desc_alcoolicas = tk.Label(self.menu_window, text="BEBIDAS ALCOÓLICAS", font=("Arial", 10))
        desc_alcoolicas.grid(row=2, column=0, sticky="ne", padx=30)

        botao_sobremesas = tk.Button(self.menu_window, image=tk_sobremesas, command=lambda: self.categorias("sobremesas"))
        botao_sobremesas.grid(row=3, column=0, pady=20, padx=50, sticky="ne")
        desc_sobremesas = tk.Label(self.menu_window, text="SOBREMESAS", font=("Arial", 10))
        desc_sobremesas.grid(row=4, column=0, sticky="ne", padx=60)

        botao_menu_chef = tk.Button(self.menu_window, image=tk_menu_chef, command=lambda: self.categorias("menu-chef"))
        botao_menu_chef.grid(row=5, column=0, pady=20, padx=50, sticky="ne")
        desc_menu_chef = tk.Label(self.menu_window, text="MENU DO CHEF", font=("Arial", 10))
        desc_menu_chef.grid(row=6, column=0, sticky="ne", padx=50)

        botao_pedidos = tk.Button(self.menu_window, image=tk_pedidos, command=self.finalize_order)
        botao_pedidos.grid(row=7, column=0, pady=20, padx=50, sticky="s")
        desc_pedidos = tk.Label(self.menu_window, text="CONFIRMAR PEDIDO", font=("Arial", 10))
        desc_pedidos.grid(row=8, column=0, sticky="s", padx=50)

        self.menu_window.mainloop()

    def categorias(self, category):
        self.category_window = tk.Tk()
        self.category_window.title(f"{category.capitalize()} - Seleção")
        self.category_window.geometry("600x600")

        tk.Label(self.category_window, text=f"Selecione {category.capitalize()}", font=("Arial", 20)).pack(pady=20)

        products = {
            "entradas": ["Salada", "Bruschetta", "Crostini", "Sopa", "Queijo Assado"],
            "pratos": ["Espaguete", "Bife", "Frango", "Peixe", "Pizza"],
            "bebidas": ["Coca-Cola", "Suco de Laranja", "Água", "Refrigerante", "Chá"],
            "alcoolicas": ["Cerveja", "Vinho", "Whisky", "Caipirinha", "Margarita"],
            "sobremesas": ["Tiramisu", "Cheesecake", "Brownie", "Sorvete", "Frutas"],
            "menu-chef": ["Risoto", "Paella", "Sushi", "Lasanha", "Fondue"]
        }
        
    

        for product in products[category]:
            tk.Button(self.category_window, text=product, font= 40, command=lambda p=product: self.add_to_order(p)).pack(pady=20)



        tk.Button(self.category_window, text="Finalizar Pedido", font= 40, command=self.finalize_order).pack(pady=20)

    def add_to_order(self, product):
        self.pedidos.append(product)
        messagebox.showinfo("Adicionado", f"{product} foi adicionado ao seu pedido.")

    def finalize_order(self):
        self.category_window.destroy()  
        self.order_window = tk.Tk()
        self.order_window.title("Seu Pedido")
        self.order_window.geometry("400x400")

        tk.Label(self.order_window, text="Seu Pedido", font=("Arial", 20)).pack(pady=20)

        for item in self.pedidos:
            tk.Label(self.order_window, text=item).pack(pady=5)

        tk.Button(self.order_window, text="Adicionar Mais Itens", command=self.menu).pack(pady=10)
        tk.Button(self.order_window, text="Confirmar Pedido", command=self.confirmar_pedido).pack(pady=10)

    def confirmar_pedido(self):
        self.order_window.destroy()
        self.confirmation_window = tk.Tk()
        self.confirmation_window.title("Pedido Confirmado")
        self.confirmation_window.geometry("400x100")
        vlw = tk.Label(self.confirmation_window, text="OBRIGADO PELO PEDIDO", font=("Arial", 20))
        vlw.grid(row=0, column=0, sticky="nw", padx=20, pady=20)

        
        self.confirmation_window.mainloop()

Sistema()


        
