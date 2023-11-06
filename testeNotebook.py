import tkinter.ttk as ttk
import tkinter as tk

window = tk.Tk()
window.geometry("800x800")
window.title("Notebook")

def ir():
    notebook.select(1)

def voltar():
    notebook.select(0)

notebook = ttk.Notebook(window)

g1 = ttk.Frame(notebook)
notebook.add(g1, text= "Guia 1")

btn1 = ttk.Button(g1, text="Ir para Guia 2", command=ir)
btn1.pack(padx=10, pady=10)

g2 = ttk.Frame(notebook)
notebook.add(g2, text= "Guia 2")

btn2 = ttk.Button(g2, text="Ir para Guia 1", command=voltar)
btn2.pack(padx=10, pady=10)

notebook.pack(pady=350)

window.mainloop()