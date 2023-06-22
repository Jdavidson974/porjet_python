from tkinter import *
from navBar.NavBar import NavBar

from pageBuilder.Pagebuilder import PageBuilder

window = Tk()
window.title("Réservation de repas")
window.geometry("1080x700")
window.minsize(480, 360)
window.iconbitmap("assets/logo.ico")
window.configure(bg="#F4B740")

# Container Page
navBarContainer = Frame(window, bg="#56B908", bd=1, relief="sunken")

contentContainer = Frame(window, bg="#FEFEFE")
navBar = NavBar(navBarContainer, contentContainer)
NavbarComponent = navBar.buildNavBar()
i = 1
for item in NavbarComponent:
    item.grid(row=0, column=i, padx=(10, 10), pady=(10, 10))
    i += i

# Content
pageBuilder = PageBuilder(contentContainer)
navBarContainer.pack(fill="x")
contentContainer.pack(fill="x", expand=YES)
pageBuilder.homePage()
window.mainloop()
