#imports
import tkinter as tk                # python 3
from tkinter import font  as tkfont # python 3
from tkinter import *
from tkinter.ttk import Progressbar
from datetime import datetime
from tkinter import ttk
from time import strftime



class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # o contêiner é onde empilharemos vários quadros
        # em cima um do outro, então o que queremos visível
        # será elevado acima dos outros,
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.geometry("800x480+00+00")
        self.minsize(width=800, height=480)
        self.maxsize(width=800, height=480)
        self.iconbitmap("top.ico")
        self.title("Menu")


        #now = datetime.now()
        #ano = now.year
        #mes = now.month
        #dia = now.day

        #dat = Label(self, text=[dia,mes,ano], font="Arial, 14",fg="white", width=50, height=1)
        #dat.place(x=450,y=0)
        #dat["bg"] = "#353535"





        def tic():
            rel['text'] = strftime('       %H:%M:%S    %D                   .')

        def tac():
            tic()
            rel.after(1000,tac)

        rel = Label(self,font=("Arial", 14, "bold"), fg="white")
        rel.place (x=580,y=0)
        tac()
        rel["bg"] = "#303535"



        self.frames = {}
        for F in (PaginaInicial, Bateria, Velocimetro, Configurações, Mode):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame


            # coloque todas as páginas no mesmo local;
            # aquele no topo da ordem de empilhamento
            # será o que estiver visível.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("PaginaInicial")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

#pagina inicial
class PaginaInicial(tk.Frame):


    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#1F1F1F" )
        self.controller = controller

        aba_1 = tk.Label(self, text="Pagina inicial", font=("Arial", 14, "bold"), fg="white", width=50, height=1)
        aba_1.place(x=0,y=0)
        aba_1["bg"] = "#353535"


        #title_1 = tk.Label(self, text="Bem Vindo", font=("Arial", 50, "bold"), fg="white")
        ##title_1.place(x=200,y=45)
        #title_1["bg"] = "#1f1f1f"

        def tic():
            rel['text'] = strftime('%H:%M')

        def tac():
            tic()
            rel.after(1000,tac)

        rel = Label(self,font=("Arial", 100, "bold"), fg="white")
        rel.place (x=250,y=170)
        tac()
        rel["bg"] = "#1F1F1F"

        fgg = Label(self,width=50, height=-3)
        fgg.place(x=250, y=320)
#botoes
        bt1 = tk.Button(self,width=11, height=4, text="Bateria",fg="white",borderwidth=0, font="Arial, ", command=lambda: controller.show_frame("Bateria"))
        bt1.place(x=0, y=25)
        bt1["bg"] = "#353535"


        bt2 = tk.Button(self,width=11, height=4, text="Velocimetro",fg="white",borderwidth=0, font="Arial, ", command=lambda: controller.show_frame("Velocimetro"))
        bt2.place(x=0, y=107)
        bt2["bg"] = "#353535"


        bt3 = tk.Button(self,width=11, height=4, text="Configurações",fg="white",borderwidth=0, font="Arial, ", command=lambda: controller.show_frame("Configurações"))
        bt3.place(x=0, y=353)
        bt3["bg"] = "#353535"


        bt4 = tk.Button(self,width=11, height=4, text="Mode",fg="white",borderwidth=0, font="Arial, ", command=lambda: controller.show_frame("Mode"))
        bt4.place(x=0, y=271)
        bt4["bg"] = "#353535"

        bt5 = tk.Button(self,width=11, height=4, text="Voltar",fg="white",borderwidth=0, font="Arial, ", command=lambda: controller.show_frame("PaginaInicial"))
        bt5.place(x=0, y=189)
        bt5["bg"] = "#353535"

        bt6 = tk.Button(self,width=11, height=2, text="sair",fg="white",borderwidth=0, font="Arial, ", command=quit )
        bt6.place(x=0, y=435)
        bt6["bg"] = "#353535"


class Bateria(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#1F1F1F" )
        self.controller = controller



        aba_1 = tk.Label(self, text="Bateria", font=("Arial", 14, "bold"), fg="white", width=50, height=1)
        aba_1.place(x=0,y=0)
        aba_1["bg"] = "#353535"

        bt1 = tk.Button(self,width=11, height=4, text="Bateria",fg="white",borderwidth=0, font="Arial, ", command=lambda: controller.show_frame("Bateria"))
        bt1.place(x=0, y=25)
        bt1["bg"] = "#353535"


        bt2 = tk.Button(self,width=11, height=4, text="Velocimetro",fg="white",borderwidth=0, font="Arial, ", command=lambda: controller.show_frame("Velocimetro"))
        bt2.place(x=0, y=107)
        bt2["bg"] = "#353535"


        bt3 = tk.Button(self,width=11, height=4, text="Configurações",fg="white",borderwidth=0, font="Arial, ", command=lambda: controller.show_frame("Configurações"))
        bt3.place(x=0, y=353)
        bt3["bg"] = "#353535"


        bt4 = tk.Button(self,width=11, height=4, text="Mode",fg="white",borderwidth=0, font="Arial, ", command=lambda: controller.show_frame("Mode"))
        bt4.place(x=0, y=271)
        bt4["bg"] = "#353535"

        bt5 = tk.Button(self,width=11, height=4, text="Voltar",fg="white",borderwidth=0, font="Arial, ", command=lambda: controller.show_frame("PaginaInicial"))
        bt5.place(x=0, y=189)
        bt5["bg"] = "#353535"

        bt6 = tk.Button(self,width=11, height=2, text="sair",fg="white",borderwidth=0, font="Arial, ", command=quit )
        bt6.place(x=0, y=435)
        bt6["bg"] = "#353535"
#pagina 2
class Velocimetro(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#1F1F1F" )
        self.controller = controller



        aba_1 = tk.Label(self, text="Velocimetro", font=("Arial", 14, "bold"), fg="white", width=50, height=1)
        aba_1.place(x=0,y=0)
        aba_1["bg"] = "#353535"

        bt1 = tk.Button(self,width=11, height=4, text="Bateria",fg="white",borderwidth=0, font="Arial, ", command=lambda: controller.show_frame("Bateria"))
        bt1.place(x=0, y=25)
        bt1["bg"] = "#353535"


        bt2 = tk.Button(self,width=11, height=4, text="Velocimetro",fg="white",borderwidth=0, font="Arial, ", command=lambda: controller.show_frame("Velocimetro"))
        bt2.place(x=0, y=107)
        bt2["bg"] = "#353535"


        bt3 = tk.Button(self,width=11, height=4, text="Configurações",fg="white",borderwidth=0, font="Arial, ", command=lambda: controller.show_frame("Configurações"))
        bt3.place(x=0, y=353)
        bt3["bg"] = "#353535"


        bt4 = tk.Button(self,width=11, height=4, text="Mode",fg="white",borderwidth=0, font="Arial, ", command=lambda: controller.show_frame("Mode"))
        bt4.place(x=0, y=271)
        bt4["bg"] = "#353535"

        bt5 = tk.Button(self,width=11, height=4, text="Voltar",fg="white",borderwidth=0, font="Arial, ", command=lambda: controller.show_frame("PaginaInicial"))
        bt5.place(x=0, y=189)
        bt5["bg"] = "#353535"

        bt6 = tk.Button(self,width=11, height=2, text="sair",fg="white",borderwidth=0, font="Arial, ", command=quit )
        bt6.place(x=0, y=435)
        bt6["bg"] = "#353535"
class Configurações(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#1F1F1F" )
        self.controller = controller




        aba_1 = tk.Label(self, text="Configurações", font=("Arial", 14, "bold"), fg="white", width=50, height=1)
        aba_1.place(x=0,y=0)
        aba_1["bg"] = "#353535"

        bt1 = tk.Button(self,width=11, height=4, text="Bateria",fg="white",borderwidth=0, font="Arial, ", command=lambda: controller.show_frame("Bateria"))
        bt1.place(x=0, y=25)
        bt1["bg"] = "#353535"


        bt2 = tk.Button(self,width=11, height=4, text="Velocimetro",fg="white",borderwidth=0, font="Arial, ", command=lambda: controller.show_frame("Velocimetro"))
        bt2.place(x=0, y=107)
        bt2["bg"] = "#353535"


        bt3 = tk.Button(self,width=11, height=4, text="Configurações",fg="white",borderwidth=0, font="Arial, ", command=lambda: controller.show_frame("Configurações"))
        bt3.place(x=0, y=353)
        bt3["bg"] = "#353535"


        bt4 = tk.Button(self,width=11, height=4, text="Mode",fg="white",borderwidth=0, font="Arial, ", command=lambda: controller.show_frame("Mode"))
        bt4.place(x=0, y=271)
        bt4["bg"] = "#353535"

        bt5 = tk.Button(self,width=11, height=4, text="Voltar",fg="white",borderwidth=0, font="Arial, ", command=lambda: controller.show_frame("PaginaInicial"))
        bt5.place(x=0, y=189)
        bt5["bg"] = "#353535"

        bt6 = tk.Button(self,width=11, height=2, text="sair",fg="white",borderwidth=0, font="Arial, ", command=quit )
        bt6.place(x=0, y=435)
        bt6["bg"] = "#353535"

class Mode(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#1f1f1f" )
        self.controller = controller



        aba_1 = tk.Label(self, text="Modos", font=("Arial", 14, "bold"), fg="white", width=50, height=1)
        aba_1.place(x=0,y=0)
        aba_1["bg"] = "#353535"

        bt1 = tk.Button(self,width=11, height=4, text="Bateria",fg="white",borderwidth=0, font="Arial, ", command=lambda: controller.show_frame("Bateria"))
        bt1.place(x=0, y=25)
        bt1["bg"] = "#353535"


        bt2 = tk.Button(self,width=11, height=4, text="Velocimetro",fg="white",borderwidth=0, font="Arial, ", command=lambda: controller.show_frame("Velocimetro"))
        bt2.place(x=0, y=107)
        bt2["bg"] = "#353535"


        bt3 = tk.Button(self,width=11, height=4, text="Configurações",fg="white",borderwidth=0, font="Arial, ", command=lambda: controller.show_frame("Configurações"))
        bt3.place(x=0, y=353)
        bt3["bg"] = "#353535"


        bt4 = tk.Button(self,width=11, height=4, text="Mode",fg="white",borderwidth=0, font="Arial, ", command=lambda: controller.show_frame("Mode"))
        bt4.place(x=0, y=271)
        bt4["bg"] = "#353535"

        bt5 = tk.Button(self,width=11, height=4, text="Voltar",fg="white",borderwidth=0, font="Arial, ", command=lambda: controller.show_frame("PaginaInicial"))
        bt5.place(x=0, y=189)
        bt5["bg"] = "#353535"

        bt6 = tk.Button(self,width=11, height=2, text="sair",fg="white",borderwidth=0, font="Arial, ", command=quit )
        bt6.place(x=0, y=435)
        bt6["bg"] = "#353535"

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
