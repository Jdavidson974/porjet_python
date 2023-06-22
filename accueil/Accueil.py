import json
from tkinter import *
import requests

from choixRepas.ChoixRepas import ChoixRepas


class Accueil:
    # Les 2 champs pour le formulaire
    usernameInput: Entry
    password: Entry
    req: requests

    def __init__(self, contentContainer: Frame) -> None:
        self.contentContainer = contentContainer
        self.req = requests

    def buildHome(self, message=None):
        # Reset container
        for widget in self.contentContainer.winfo_children():
            widget.pack_forget()
        # TITRE DE LA PAGE
        title = Label(
            self.contentContainer,
            text="Page d'accueil",
            bg="#FEFEFE",
            font=("Arial", 30),
        )
        title.pack(
            pady=(10, 10),
        )
        # Container parent
        mainContainer = Frame(
            self.contentContainer,
            bg="#FEFEFE",
        )
        # Container gauche
        containerL = Frame(mainContainer, bg="#FEFEFE")
        usernameLabel = Label(containerL, text="Username", bg="#FEFEFE")
        self.usernameInput = Entry(containerL, bg="#FEFEFE")
        usernameLabel.pack(
            side="left",
            padx=(10, 10),
        )
        self.usernameInput.pack(side="left", padx=(10, 10))
        # Container droite
        containerR = Frame(
            mainContainer,
            bg="#FEFEFE",
        )
        passwordLabel = Label(containerR, text="Password", bg="#FEFEFE")
        self.password = Entry(containerR, bg="#FEFEFE", show="●")
        passwordLabel.pack(
            side="left",
            padx=(10, 10),
        )
        self.password.pack(side="left", padx=(10, 10))

        # Insertion des container gauche et droite

        containerSubmit = Frame(mainContainer, mainContainer, bg="#FEFEFE")
        # Button submit
        btnSubmit = Button(
            containerSubmit,
            text="Se connecter",
            command=self.submit,
        )
        if message:
            a = Label(mainContainer, text=message, bg="#FEFEFE")
            a.pack()
        btnSubmit.pack(side="bottom")
        containerSubmit.pack(side="bottom", fill="x", pady=(10, 10))
        containerL.pack(side="left", pady=(10, 10))
        containerR.pack(side="right", pady=(10, 10))
        # Insertion du container parent
        mainContainer.pack(expand=YES)

    def submit(
        self,
    ):
        usernameValue = self.usernameInput.get()
        passwordValue = self.password.get()
        data = {"email": usernameValue, "password": passwordValue}
        headers = {"Content-type": "application/json", "Accept": "text/plain"}
        r = self.req.post(
            "https://monbarquette.formaterz.fr/authentication_token",
            json.dumps(data),
            headers=headers,
        )
        print(r.status_code)
        # PASSER LA REQ
        if r.status_code == 200:
            result = r.json()
            token = result["token"]
            pageChoixRepas = ChoixRepas(self.contentContainer, token).buildRepasPage()
        else:
            message = "Identifiant ou mot de passe incorect"
            self.buildHome(message)
