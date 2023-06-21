from tkinter import *


class PageBuilder :
    # Constructor 
    def __init__(self,canvas : Canvas) -> None:
        self.canvas = canvas
    # Page d'accueil 
    def homePage(self) :

        for widget in self.canvas.winfo_children():
            widget.pack_forget()
        title = Label(self.canvas,text="Page d'accueil")
        button = Button(self.canvas,command=self.choixRepas , text="Choisir mon repas")
        title.pack()
        button.pack()

    # Page choix des repas 
    def choixRepas(self) :
        for widget in self.canvas.winfo_children():
            widget.pack_forget()
        title = Label(self.canvas,text="Choix du repas")
        buttonAccueil = Button(self.canvas,command=self.homePage , text="Page d'accueil")
        buttonReserver = Button(self.canvas,command=self.reserver , text="Reserver")
        title.pack()
        buttonAccueil.pack()
        buttonReserver.pack()

    # Page reservation 
    def reserver(self) :
        for widget in self.canvas.winfo_children():
            widget.pack_forget()
        title = Label(self.canvas,text="Reservation")
        buttonAccueil = Button(self.canvas,command=self.homePage , text="Page d'accueil")
        buttonRepas = Button(self.canvas,command=self.choixRepas , text="Choisir mon repas")
        title.pack()
        buttonAccueil.pack()
        buttonRepas.pack()
