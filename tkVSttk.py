import tkinter.ttk as ttk
import tkinter as tk

janela = tk.Tk()
janela.geometry("400x400")

# tk VS ttk
btn1 = tk.Button(janela, text="Botão Antigo").pack()
btn2 = ttk.Button(janela, text="Botão Novo").pack()

state_br = ["Bahia", "São Paulo", "Brasilia", "Rio de Janeiro", "Goiais", "Acre"]

def mostrar():
    print(cbobx.get())

cbobx = tk.StringVar()

combobox = ttk.Combobox(janela, values=state_br, state="readonly", textvariable=cbobx)
combobox.pack(padx=75, pady=75)

btn  = ttk.Button(janela, text="executar", command=mostrar).pack()

janela.mainloop()
