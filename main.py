from tkinter import *

window = Tk()
window.title("Réservation de repas")
window.geometry("1080x700")
window.minsize(480,360)


# Page d'accueil 
def homePage() :
    
    for widget in canvas.winfo_children():
        widget.pack_forget()
    title = Label(canvas,text="Page d'accueil")
    button = Button(canvas,command=choixRepas , text="Choisir mon repas")
    title.pack()
    button.pack()

def choixRepas() :
    for widget in canvas.winfo_children():
        widget.pack_forget()
    title = Label(canvas,text="Choix du repas")
    buttonAccueil = Button(canvas,command=homePage , text="Page d'accueil")
    buttonReserver = Button(canvas,command=reserver , text="Reserver")
    title.pack()
    buttonAccueil.pack()
    buttonReserver.pack()

def reserver() :
    for widget in canvas.winfo_children():
        widget.pack_forget()
    title = Label(canvas,text="Reservation")
    buttonAccueil = Button(canvas,command=homePage , text="Page d'accueil")
    buttonRepas = Button(canvas,command=choixRepas , text="Choisir mon repas")
    title.pack()
    buttonAccueil.pack()
    buttonRepas.pack()

# Container Page 
container = Frame(window)

# Canvas 
canvas = Canvas(container)
canvas.pack()
container.pack(expand=YES)
homePage()
window.mainloop()
