from tkinter import *


class ChoixRepas:
    apiUrl = "https://www.themealdb.com/api/json/v1/1/random.php"

    def __init__(self, canvas: Canvas) -> None:
        self.canvas = canvas
        # Build la page choix des repas

    def buildRepasPage(self):
        title = Label(self.canvas, text="Choix des repas", bg="#FEFEFE")
        title.pack()
