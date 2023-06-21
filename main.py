from tkinter import *
from navBar.NavBar import NavBar

from pageBuilder.Pagebuilder import PageBuilder

window = Tk()
window.title("Réservation de repas")
window.geometry("1080x700")
window.minsize(480,360)
window.iconbitmap("assets/logo.ico")
window.configure(bg="#F4B740")

# Container Page 
container = Frame(window,bg="blue")
navBarContainer = Frame(window,bg="#56B908", bd=1 , relief="sunken")

canvas = Canvas(container,bg="#FEFEFE")
navBar = NavBar(navBarContainer,canvas)
NavbarComponent = navBar.buildNavBar()
i=1
for item in NavbarComponent :
    item.grid(row=0,column=i,padx=(10, 10),pady=(10, 10))
    i+=i
# Canvas 
canvas.pack(fill="both")
navBarContainer.pack(fill="x")
container.pack(expand=YES,fill="x")
pageBuilder = PageBuilder(canvas)
pageBuilder.homePage()
window.mainloop()
