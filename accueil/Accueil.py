from tkinter import *
class Accueil() :
    def __init__(self,canvas:Canvas) -> None:
        self.canvas = canvas
    def buildHome(self) :
        title = Label(self.canvas,text="Page d'accueil",bg="#FEFEFE")
        title.pack()

        
        