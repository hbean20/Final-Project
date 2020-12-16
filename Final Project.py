from tkinter import *

# LOGIN FUNCTIONS
def login():
    print("p")




# MAIN WINDOW
window = Tk()

title = Label(window, text="Contacts", bg="black", fg="white")
title.pack(side=TOP, fill=X)

topFrame = Frame(window, width=300, height=300)
topFrame.pack()
bottomFrame = Frame(window, width=300, height=300)
bottomFrame.pack(side=BOTTOM)

login = Button(bottomFrame, text="Log in",bg="white", fg="blue")
makeAccount = Button(bottomFrame, text="Create a new log in",bg="white", fg="blue")

login.pack()
makeAccount.pack()




window.mainloop()

# LOGIN WINDOW
loginPage = Tk()

userLabel = Label(loginPage, text="Username")
passLabel = Label(loginPage, text="Password")
userEntry = Entry(loginPage)
passEntry = Entry(loginPage)

userLabel.grid(row=0, sticky=E)
passLabel.grid(row=1, sticky=E)

userEntry.grid(row=0, column=1)
passEntry.grid(row=1, column=1)

loginPage.mainloop()
