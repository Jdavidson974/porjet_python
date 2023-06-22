from tkinter import *

from pageBuilder.Pagebuilder import PageBuilder


class NavBar:
    def __init__(self, container: Frame, contentContainer: Frame) -> None:
        self.container = container
        self.contentContainer = contentContainer

    # Create navBar
    def buildNavBar(self) -> tuple[Button]:
        pageBuilder = PageBuilder(self.contentContainer)
        buttonAccueil = Button(
            self.container, text="Accueil", command=pageBuilder.homePage, bg="#FEFEFE"
        )
        # buttonChoixRepas = Button(self.container,text="Choix des repas", command=pageBuilder.choixRepas, bg="#FEFEFE")
        return (buttonAccueil,)
