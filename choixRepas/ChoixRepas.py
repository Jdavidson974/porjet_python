from tkinter import *
import requests


class ChoixRepas:
    apiUrl = " https://monbarquette.formaterz.fr/api/repas"
    req: requests

    def __init__(self, contentContainer: Frame, token: str) -> None:
        self.contentContainer = contentContainer
        self.req = requests
        self.token = token
        # Build la page choix des repas

    def buildRepasPage(self):
        headers = {
            "Content-type": "application/json",
            "Accept": "text/plain",
            "Authorization": "Bearer " + self.token,
        }
        request = self.req.get(self.apiUrl)
        result: tuple = request.json()
        # print(result)
        # Reset container
        for widget in self.contentContainer.winfo_children():
            widget.pack_forget()
        # Title
        title = Label(
            self.contentContainer,
            text="Page Choix des repas",
            bg="#FEFEFE",
            font=("Arial", 30),
        )
        title.pack()
        contentContainer = Frame(self.contentContainer, bg="#FEFEFE")
        for repas in result["hydra:member"]:
            cardRepas = Frame(
                contentContainer, bg="#FEFEFE", borderwidth=3, relief="raised"
            )
            name = Label(cardRepas, text=repas["name"], bg="#FEFEFE")
            # description = Label(cardRepas, text=repas["descrition"])
            name.pack(padx=(10, 10), fill="x")
            if repas["disponible"]:
                dispo = Label(
                    cardRepas, text="Cette barquette est disponible", bg="#FEFEFE"
                )
                dispo.pack()
            else:
                indispo = Label(
                    cardRepas, text="Cette barquette n'est pas disponible", bg="#FEFEFE"
                )
                indispo.pack()
            # description.pack()
            cardRepas.pack(side="left", padx=(10, 10), expand=YES)
        contentContainer.pack(expand=YES)
