import tkinter.ttk as ttk
import tkinter as tk

janela = tk.Tk()
janela.title = ("Notebook Example")
janela.geometry("800x800")

# Notebook
notebook = ttk.Notebook(janela)

# GUIDE ONE
guide1 = ttk.Frame(notebook)
notebook.add(guide1, text="Guia 1")

label1 = ttk.Label(guide1, text="Conteudo da Guia 1")
label1.pack(padx=10, pady=10)

# GUIDE TWO
guide2 = ttk.Frame(notebook)
notebook.add(guide2, text="Guia 2")

label2 = ttk.Label(guide2, text="Conteudo da Guia 2")
label2.pack(padx=10, pady=10)

# GUIDE THREE
guide3 = ttk.Frame(notebook)
notebook.add(guide3, text="Guia 3")

label3 = ttk.Label(guide3, text="Conteudo da Guia 3")
label3.pack(padx=10, pady=10)

notebook.pack(pady=340)

janela.mainloop()