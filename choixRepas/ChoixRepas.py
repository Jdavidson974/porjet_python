from tkinter import *
class ChoixRepas() :
    def __init__(self,canvas:Canvas) -> None:
        self.canvas = canvas
        # Build la page choix des repas 
    def buildRepasPage(self) :
        title = Label(self.canvas,text="Choix des repas",bg="#FEFEFE")
        title.pack()
        
        