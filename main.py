from tkinter import *
import tkinter.messagebox as tkMessageBox
import os
import tkinter.filedialog as fdlg
from tkinter import ttk
import pandas as pd
from Usuarios2 import Usuarios


def saindo():
	result = tkMessageBox.askquestion("", "Confirma a saída?", icon='question')
	if result=='yes':
		os._exit(1)
	else:
		pass


def baixardor():
    try:
        progress1['value']+=10
        tela.update()

        #aqui seleciona a pasta a ser colocada o novo arquivo
        opcoes = {}                # as opções são definidas em um dicionário
        opcoes['initialdir'] = ''    # será o diretório atual
        opcoes['parent'] = tela
        opcoes['title'] = 'Local onde o Banco se encontra'
        caminhoinicial = fdlg.askdirectory(**opcoes)    
        user = Usuarios()
        resposta = user.relatorios(caminhoinicial,tela)
        #print(caminhoinicial)
        tkMessageBox.showinfo('Resposta ', resposta)
        progress1.stop()
    except:
        tkMessageBox.showinfo('Resposta ','Não efetuado, favor tentar novamente!')
        progress1.stop()
def progresso():
	progress1.start(10)
	baixardor()

tela = Tk()
tela.title("Conversor de Banco Para Excel")
tela.geometry("800x500+400+0")
tela.resizable(width=False, height=False)
tela['bg'] = "OrangeRed"
tela.iconphoto(True, PhotoImage(file='./arquivos/foto.png'))
image=PhotoImage(file='./arquivos/foto.png')

robozinho = Label(tela, image = image,width=800, height=500,bg ="white")
robozinho.grid(row=10,columnspan =10)

lbltitul = Label(tela, text="Conversor de Sqlite Para Excel",bg="MediumTurquoise",fg="black", font=('arial',25,'bold'))
lbltitul.place(relx = 0.15, rely = 0.02)
btinicio = Button(tela, text = " Iniciar  ",width=15, height=1,bd =5 ,bg="MediumAquamarine",fg="black", font=('arial',25,'bold'),command=progresso)
btinicio.place(relx = 0.05, rely = 0.15)

btsair = Button(tela, text = "   Sair   " ,width=15, height=1,bd = 5, bg="MediumAquamarine",fg="black", font=('arial',25,'bold'),command=saindo)
btsair.place(relx = 0.6, rely = 0.15)

#importante para progressbar
s = ttk.Style() 
s.theme_use('default') 
s.configure("SKyBlue1.Horizontal.TProgressbar", foreground='DarkSeaGreen3', background='white')

progress1 =ttk.Progressbar(tela, orient=VERTICAL, length=450, style="SKyBlue1.Horizontal.TProgressbar",mode='determinate')
progress1.place(relx=0.005, rely = 0)

tela.mainloop()