from tkinter import *

from choixRepas.ChoixRepas import ChoixRepas

from accueil.Accueil import Accueil


class PageBuilder :
    # Constructor 
    def __init__(self,canvas : Canvas) -> None:
        self.canvas = canvas
    # Page d'accueil 
    def homePage(self) :

        for widget in self.canvas.winfo_children():
            widget.pack_forget()
        accueil = Accueil(self.canvas)
        accueil.buildHome()

    # Page choix des repas 
    def choixRepas(self) :
        for widget in self.canvas.winfo_children():
            widget.pack_forget()
        choixRepas = ChoixRepas(self.canvas)
        choixRepas.buildRepasPage()
        
    # Page reservation 
    def reserver(self) :
        for widget in self.canvas.winfo_children():
            widget.pack_forget()
        title = Label(self.canvas,text="Reservation")
        title.pack()
