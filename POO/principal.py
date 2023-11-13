from classes import (
    Automoveis,
)
import tkinter as tk
import tkinter.ttk as ttk

window = tk.Tk()
window.geometry("800x600")
window.title("Cadastro de Veiculos")
window.resizable(False, False)

# Rótulos
lblMarca = tk.Label(window, text="Informe a Marca do Veículo: ")
lblMarca.grid(row=0, column=0)

lblModelo = tk.Label(window, text="Informe o Modelo do Veículo: ")
lblModelo.grid(row=1, column=0)

lblCor = tk.Label(window, text="Informe a Cor do Veículo: ")
lblCor.grid(row=2, column=0)

lblMax = tk.Label(window, text="Informe a Velocidade Maxima do Veículo: ")
lblMax.grid(row=3, column=0)


# Caixas de texto para as Lables
txtMarca = tk.Entry(window)
txtMarca.grid(row=0, column=1)

txtModelo = tk.Entry(window)
txtModelo.grid(row=1, column=1)

txtCor = tk.Entry(window)
txtCor.grid(row=2, column=1)

max = tk.IntVar()
txtMax = ttk.Entry(window, textvariable=max)
txtMax.grid(row=3, column=1)

def execute():
    chevette = Automoveis(txtMarca, txtModelo, txtCor, max.get())
    chevette.ligado = True  # Ligando o Chevette...
    # for a in range(4):
    chevette.acelerar(200)
    print("Velocidade Atual: ", chevette.veloAtual)  # VeloMax
    print(chevette.veloMax)

btnExecute = tk.Button(window, text="Cadastrar", command=execute)
btnExecute.place(x=15, y=140)

# Método para renderizar em LOOP a janela principal na Tela:
window.mainloop()




