from tkinter import *

from pageBuilder.Pagebuilder import PageBuilder

window = Tk()
window.title("Réservation de repas")
window.geometry("1080x700")
window.minsize(480,360)

# Container Page 
container = Frame(window)

# Canvas 
canvas = Canvas(container)
canvas.pack()
container.pack(expand=YES)
pageBuilder = PageBuilder(canvas)
pageBuilder.homePage()
window.mainloop()
