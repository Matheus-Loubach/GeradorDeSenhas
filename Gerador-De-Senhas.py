from tkinter import *
import string as st
import numpy as np


letras = st.ascii_letters
numeros = st.digits
especial = st.punctuation
algoritimo = (numeros+letras+especial)


class Application:
    def __init__(self, master=None):
        self.fontePadrao = ("Arial", "10", "")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()
       
        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 20
        self.segundoContainer.pack()

        self.terceiroContainer = Frame(master)
        self.terceiroContainer["pady"] = 20
        self.terceiroContainer.pack()

        self.titulo = Label(self.primeiroContainer, text="Gerador de senhas")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()

        self.tamanhoLabel = Label(self.segundoContainer,text="Qual o tamanho da senha você deseja?", font=self.fontePadrao)
        self.tamanhoLabel.pack(side=TOP)

        self.tamanho = Entry(self.segundoContainer)
        self.tamanho["width"] = 35
        self.tamanho["font"] = self.fontePadrao
        self.tamanho.pack(side=LEFT)

        self.autenticar = Button(self.terceiroContainer)
        self.autenticar["text"] = "Criar Senha"
        self.autenticar["font"] = ("Calibri", "8")
        self.autenticar["bg"] = ("black")
        self.autenticar["fg"] = ("white")
        self.autenticar["width"] = 12
        self.autenticar["command"] = self.verificaSenha
        self.autenticar.pack()


        self.mensagem = Label(self.terceiroContainer, text="", font=self.fontePadrao)
        self.mensagem.pack()

    #Método verificar senha
    def verificaSenha(self):
        try:
         tamanhoSenha =  (int(self.tamanho.get()))
           
         if tamanhoSenha >= 8 and tamanhoSenha <= 100:
            senha = np.random.choice(list(algoritimo),tamanhoSenha)
            self.mensagem["text"] = ''.join(senha)
         else:
             self.mensagem["text"] = "Min 10 de Tamanho / Max 100 de Tamanho"
        except ValueError:
         self.mensagem["text"] = "Somente números"

root = Tk()
Application(root)
root.title('Gerador De Senhas')
root.mainloop()

