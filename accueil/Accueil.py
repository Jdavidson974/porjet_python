from tkinter import *
class Accueil() :
    def __init__(self,contentContainer:Frame) -> None:
        self.contentContainer = contentContainer
    def buildHome(self) :
        title = Label(self.contentContainer,text="Page d'accueil",bg="#FEFEFE")
        title.pack()
        mainContainer = Frame(self.contentContainer,bg="#FEFEFE")
        containerL = Frame(mainContainer,bg="#FEFEFE")
        usernameLabel = Label(containerL,text="Username",bg="#FEFEFE")
        usernameInput = Entry(containerL,bg="#FEFEFE")
        usernameLabel.pack(side="left",padx=(10,10),)
        usernameInput.pack(side="left",padx=(10,10))
        containerR = Frame(mainContainer,bg="#FEFEFE",)
        passwordLabel = Label(containerR,text="Password",bg="#FEFEFE")
        password = Entry(containerR,bg="#FEFEFE")
        passwordLabel.pack(side="left",padx=(10,10),)
        password.pack(side="left",padx=(10,10))
        containerL.pack(side="left")
        containerR.pack(side="right")
        mainContainer.pack(expand=YES)
        
        