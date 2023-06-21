from tkinter import *

from pageBuilder.Pagebuilder import PageBuilder
class NavBar :
    def __init__(self,container:Frame,canvas:Canvas) -> None:
        self.container = container
        self.canvas = canvas

    # Create navBar 
    def buildNavBar(self) -> tuple[Button] :
        pageBuilder = PageBuilder(self.canvas)
        buttonAccueil = Button(self.container,text="Accueil", command=pageBuilder.homePage, bg="#FEFEFE")
        buttonChoixRepas = Button(self.container,text="Choix des repas", command=pageBuilder.choixRepas, bg="#FEFEFE")
        return buttonAccueil,buttonChoixRepas
