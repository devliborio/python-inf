import tkinter.ttk as ttk
import tkinter as tk

janela = tk.Tk()
janela.geometry("400x400")

# tk VS ttk
btn1 = tk.Button(janela, text="Botão Antigo").pack()
btn2 = ttk.Button(janela, text="Botão Novo").pack()

janela.mainloop()