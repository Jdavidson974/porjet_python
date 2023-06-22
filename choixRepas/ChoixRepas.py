from tkinter import *


class ChoixRepas:
    apiUrl = "https://www.themealdb.com/api/json/v1/1/random.php"

    def __init__(self, contentContainer: Frame) -> None:
        self.contentContainer = contentContainer
        # Build la page choix des repas

    def buildRepasPage(self):
        title = Label(self.contentContainer, text="Choix des repas", bg="#FEFEFE")
        title.pack()
