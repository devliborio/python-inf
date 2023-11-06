# Interface Python, com disponibilidade para novos temas. (TkInter)

import tkinter as tk  # ! Importando o tkInter
import tkinter.messagebox as msgbox  # ! Pacote do tkInter que exibe caixas de mensagens (Modulo)

# ! Instanciar um objeto 'Master Window' -> Janela Principal.
window = tk.Tk()  # Essa janela principal é criada a partir desse método ou função Tk().
window.title("Root v1.0")  # Titulo da Master Window
percentual = 60 / 100  # Porcentagem pré ajustada definir o tamanho da janela.
sizeWindow = f"{int(window.winfo_screenwidth() * percentual)}x{int(window.winfo_screenheight() * percentual)}"  # Pegando Largura e Altura do monitor do Usuário.
window.geometry(sizeWindow)  # Método para ajustar a largura e altura da janela da Master Window.
window.resizable("False", "False")  # Redimensionável(largura, altura)

titleClient = tk.Label(window, text="Digite o nome do Cliente: ")
titleClient.place(x=10, y=10)
boxClient = tk.Entry(window)
boxClient.place(x=15, y=30)
ageClient = tk.Label(window, text="Digite a idade do Cliente")
ageClient.place(x=10, y=50)
boxClient = tk.Entry(window)
boxClient.place(x=15, y=70)

gender0 = tk.Radiobutton(window, text="Masculine").place(x=15,y=100)


def save():
    msgbox.showinfo("Root v1.0", "Salvamento concluído!")


def danger():
    a = msgbox.askyesnocancel("DIE OR LIVE?", "Confirma?")

    if a:
        msgbox.showinfo("Root v1.0", "You Died!")
    elif a == None:
         msgbox.showinfo("Root v1.0", "You cancelled!")
    else:
        msgbox.showinfo("Root v1.0", "You lived!")

btnSave = tk.Button(window, text="Save Infos", command=save)
btnSave.place(x=15, y=140)
btnQuestion = tk.Button(window, text="Danger Button", command=danger)
btnQuestion.place(x=15, y=170)


window.mainloop()  # Deixando a janela renderizando em loop
