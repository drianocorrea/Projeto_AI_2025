import tkinter as interface
from tkinter import *
from tkinter import ttk
from mainSearch import mainSearch

menu = interface.Tk()

choicesorig = ['ARAD', 'BUCARESTE', 'CRAIOVA', 'DOBRETA', 'EFORIE', 'FAGARAS', 'GIORGIU', 'HIRSOVA', 'IASI', 'LUGOJ',
               'MEHADIA', 'NEAMT', 'ORADEA', 'PITESTI', 'RIMNICUVILCEA', 'SIBIU', 'TIMISOARA', 'URZICENI', 'VASLUI', 'ZERIND']
choicesobj = ['ARAD', 'BUCARESTE', 'CRAIOVA', 'DOBRETA', 'EFORIE', 'FAGARAS', 'GIORGIU', 'HIRSOVA', 'IASI', 'LUGOJ',
              'MEHADIA', 'NEAMT', 'ORADEA', 'PITESTI', 'RIMNICUVILCEA', 'SIBIU', 'TIMISOARA', 'URZICENI', 'VASLUI', 'ZERIND']
choicesmet = ['AMPLITUDE', 'PROFUNDIDADE', 'PROFUNDIDADE_LIMITADA',
              'APROFUNDAMENTO_ITERATIVO', 'BIDIRECIONAL']


class Application():
    def __init__(self):
        self.menu = menu
        self.tela()
        self.frames()
        self.combobox()
        self.botoes()
        self.label_resultado()
        self.resultado()
        self.valorcusto()
        menu.mainloop()

    def tela(self):
        self.menu.title("Cálculo de caminho ponderado")
        self.menu.iconbitmap("icone.ico")
        self.menu.geometry("640x480")
        self.menu.configure(bg="lightblue")
        self.menu.resizable(False, False)
        self.label = Label(menu, text="Bem-vindo ao meu aplicativo!",
                           bg="lightblue", font=("Arial", 14))
        self.label.pack(pady=15)

    def combobox(self):
        self.dropdownini = ttk.Combobox(self.menu, values=choicesorig,
                                        state="readonly", width=20)
        self.dropdownini.place(
            relwidth=0.25, relheight=0.05, relx=0.18, rely=0.1)
        self.dropdownini.set("Selecione Origem")
        self.dropdownfim = ttk.Combobox(self.menu, values=choicesobj,
                                        state="readonly", width=20)
        self.dropdownfim.place(
            relwidth=0.25, relheight=0.05, relx=0.18, rely=0.18)
        self.dropdownfim.set("Selecione Destino")
        self.dropdownmet = ttk.Combobox(self.menu, values=choicesmet,
                                        state="readonly", width=20)
        self.dropdownmet.place(
            relwidth=0.25, relheight=0.05, relx=0.18, rely=0.26)
        self.dropdownmet.set("Selecione Método")

    def botoes(self):
        self.btcalc = Button(self.menu, text="Calcular",
                             width=20, bg="blue", fg="white", command=self.valororig)
        self.btcalc.config(font=("Arial", 12, "bold"))
        self.btcalc.place(
            relwidth=0.25, relheight=0.08, relx=0.18, rely=0.4)
        self.btcalc.config(state=NORMAL)

    def label_resultado(self):
        self.labelresultado = Label(self.menu, text="CAMINHO:",
                                    bg="lightblue", font=("Arial", 12), border=10)
        self.labelresultado.place(
            relwidth=0.25, relheight=0.05, relx=-0.04, rely=0.62)
        # self.labelresultado.config(state=NORMAL)

    def valororig(self):
        self.custo.configure(state="normal")  # Enable editing temporarily
        self.custo.delete("1.0", END)  # Clear previous text
        self.result.configure(state="normal")  # Enable editing temporarily
        self.result.delete("1.0", END)  # Clear previous text
        origem = self.dropdownini.get()
        destino = self.dropdownfim.get()
        calculo = self.dropdownmet.get()
        #mainSearch(self, origem, destino, calculo)
        print(origem)
        print(destino)
        #print(calculo)
        testa = mainSearch(self,calculo)
        if testa == False:
            mostra = "Caminho não encontrado"
            self.result.insert("1.0", mostra)
        else:
            mostra = mainSearch(self, origem, destino, calculo)
            self.result.insert("1.0", mostra)
        self.custo.insert("1.0", mostra)
        self.result.configure(state="disable")  # Enable editing temporarily
        self.custo.configure(state="disable")  # Enable editing temporarily

    def valorcusto(self):
        self.custo = Text(self.frame1, width=20, bd=0)
        self.custo.configure(state="disable")
        # self.custo.insert("1.0","Calcular custo")
        # self.custo.configure(takefocus=False,)  # Disable focus on the Text widget
        self.custo.pack(pady=10, padx=10)

    def resultado(self):
        self.result = Text(self.menu, height=10, width=50, bd=0, bg="white",
                           highlightbackground="blue", highlightthickness=2)
        # Disable focus on the Text widget
        self.result.configure(takefocus=False,)
        self.result.configure(state="disable")
        # self.result.pack(pady=10, padx=100, fill=BOTH, expand=True)

        """self.result = Text(self.menu, height=10, width=50)
        self.result.insert(mainSearch(self, path))
        self.result.configure(state="disabled")"""
        self.result.place(relwidth=0.75, relheight=0.3,
                          relx=0.18, rely=0.63)

    def frames(self):
        self.frame1 = Frame(self.menu, bd=4, bg="white",
                            highlightbackground="blue", highlightthickness=2)
        self.frame1.place(relwidth=0.45, relheight=0.5, relx=0.48, rely=0.1)
        # self.result.


Application()
