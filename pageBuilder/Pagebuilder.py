from tkinter import *

from choixRepas.ChoixRepas import ChoixRepas

from accueil.Accueil import Accueil


class PageBuilder:
    # Constructor
    def __init__(self, contentContainer: Frame) -> None:
        self.contentContainer = contentContainer

    # Page d'accueil
    def homePage(self):
        accueil = Accueil(self.contentContainer)
        accueil.buildHome()

    # Page choix des repas
    def choixRepas(self):
        choixRepas = ChoixRepas(self.contentContainer)
        choixRepas.buildRepasPage()

    # Page reservation
    def reserver(self):
        for widget in self.contentContainer.winfo_children():
            widget.pack_forget()
        title = Label(self.contentContainer, text="Reservation")
        title.pack()
