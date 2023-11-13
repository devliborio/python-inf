# Revisão TkInter
# - Instalação: pip instal tkinter

# - Iportação da Biblioteca
import tkinter as tk

# Master Window
janela = tk.Tk()
janela.geometry("800x600")
janela.title("Main Window")
janela.resizable(False, False)

# Rótulo
lblLogin = tk.Label(janela, text="Informe o ID: ")
lblLogin.grid(row=0,column=0)
lblPassword = tk.Label(janela, text="Informe a senha: ")
lblPassword.grid(row=1,column=0)

# Caixa de Texto do LOGIN:
txtLogin = tk.Entry(janela)
txtLogin.grid(row=0,column=1)
txtPassword = tk.Entry(janela, show="*")
txtPassword.grid(row=1,column=1)

# Botão:
btnConfirma = tk.Button(janela, text="Login")
btnConfirma.grid(row=3,column=1,sticky='we')

# Método para renderizar em LOOP a janela principal na Tela:
janela.mainloop()