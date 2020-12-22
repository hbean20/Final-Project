from tkinter import *
# Hayden Bean
# CIS 153
# 12/21/2020
# Contact Book
def create_contact_list(): # Creates contact list above input section
    global nameFrame1
    global phoneFrame1
    global emailFrame1
    global groupFrame1
    global buttonFrame1
    global addFrame1

    addFrame1 = Frame(contactPage, width=100, height=100)  # Formats contact list section
    addFrame1.pack(side=BOTTOM)
    addTitle1 = Label(addFrame1, text="Contact List", bg="black", fg="white")
    addTitle1.pack(side=TOP, fill=X)

    nameFrame1 = Frame(addFrame1, width=100, height=10)  # Creates frames to fit the labels into
    nameFrame1.pack(side=LEFT)
    phoneFrame1 = Frame(addFrame1, width=100, height=10)
    phoneFrame1.pack(side=LEFT)
    emailFrame1 = Frame(addFrame1, width=100, height=10)
    emailFrame1.pack(side=LEFT)
    groupFrame1 = Frame(addFrame1, width=100, height=10)
    groupFrame1.pack(side=LEFT)
    Label(nameFrame1, text="Name").pack()
    Label(phoneFrame1, text="Phone").pack()
    Label(emailFrame1, text="Email").pack()
    Label(groupFrame1, text="Group").pack()

# STRING TO LIST - Converts the string taken from the adding contact to a list
def string_converter(str):
    listy = list(str.split(","))
    return listy

# REFRESH CONTACTS - refreshes contacts to update for newly added contacts
def refresh_contacts():
    addFrame1.destroy()
    create_contact_list() # calls function to recreate contact format
    userPin = pin1
    fhand = open(userPin+".txt") # loops through file to add contacts in correct places without duplicates
    for line in fhand:
        line = line.rstrip()
        listy = string_converter(line)
        Label(nameFrame1, text=listy[0], bg="white", width=18).pack(side=TOP, fill=X)
        Label(phoneFrame1, text=listy[1], bg="white", width=18).pack(side=TOP, fill=X)
        Label(emailFrame1, text=listy[2], bg="white", width=18).pack(side=TOP, fill=X)
        Label(groupFrame1, text=listy[3], bg="white", width=18).pack(side=TOP, fill=X)




    fhand.close()
# ADDING CONTACTS - formats contacts correctly to be stored in the file
def add_contact():
    userPin = pin1
    addName = name.get()
    addPhone = phone.get()
    addEmail = email.get()
    addGroup = group.get()

    if addName == "":
        addName = "-"
    if addPhone == "":
        addPhone = "-"
    if addEmail == "":
        addEmail = "-"
    if addGroup == "":
        addGroup = "-"

    fhand = open(userPin+".txt", "a")  # writes the correctly formatted contact into the file
    fhand.write(addName+","+addPhone+","+addEmail+","+addGroup+",\n")
    fhand.close()

    nameEntry.delete(0, END) # clears text boxes
    phoneEntry.delete(0, END)
    emailEntry.delete(0, END)
    groupEntry.delete(0, END)

# CONTACT PAGE
def contact_page(userPin): # main page after logging in

    global contactPage
    contactPage = Tk()
    contactPage.title("Contacts")
    global pin1
    pin1 = userPin


    # CONTACT DISPLAY

    refreshContacts = Button(contactPage, text="Refresh", bg="white", fg="blue", command=refresh_contacts).pack() # creates refresh button

    addFrame = Frame(contactPage, width=500, height=500) # formats the contact adding section
    addFrame.pack(side=BOTTOM)
    addTitle = Label(addFrame, text="Add Contacts", bg="black", fg="white")
    addTitle.pack(side=TOP, fill=X)

    nameFrame = Frame(addFrame, width=100, height=500)
    nameFrame.pack(side=LEFT)
    phoneFrame = Frame(addFrame, width=100, height=500)
    phoneFrame.pack(side=LEFT)
    emailFrame = Frame(addFrame, width=100, height=500)
    emailFrame.pack(side=LEFT)
    groupFrame = Frame(addFrame, width=100, height=500)
    groupFrame.pack(side=LEFT)
    buttonFrame = Frame(addFrame, width=100, height=500)
    buttonFrame.pack(side=LEFT)

    global name  # creates space to store newly input contact information
    global phone
    global email
    global group
    name = StringVar()
    phone = StringVar()
    email = StringVar()
    group = StringVar()

    global nameEntry
    global phoneEntry
    global emailEntry
    global groupEntry
    nameEntry = Entry(nameFrame, textvariable = name)
    nameEntry.pack()
    Label(nameFrame, text="Name").pack()
    phoneEntry = Entry(phoneFrame, textvariable = phone)
    phoneEntry.pack()
    Label(phoneFrame, text="Phone Number").pack()
    emailEntry = Entry(emailFrame, textvariable = email)
    emailEntry.pack()
    Label(emailFrame, text="Email").pack()
    groupEntry = Entry(groupFrame, textvariable = group)
    groupEntry.pack()
    Label(groupFrame, text="Group").pack()
    addButton = Button(buttonFrame, text="Add", bg="white", fg="blue", command = add_contact)
    addButton.pack()

    create_contact_list() # calls to create contact list for the first time





# LOGIN FUNCTIONS
def login_pin():   # checks to make sure the pin entered is in the system
    checkPin = pin.get()
    count = 0

    fhand = open("registry.txt")
    for line in fhand:
        line = line.rstrip() # loops through registry to see if
        if line == checkPin:
            count = count + 1
    fhand.close()
    if count > 0: # if its there opens contact window
        pinEntry.delete(0, END)
        window.destroy()
        contact_page(checkPin)
    else:
        error = Tk()
        error.title("ERROR")

        Label(error, width=30, height=5, text="ERROR: Could not find pin.").pack()


def login(): # login page
    global loginPage
    loginPage = Toplevel(window)
    loginPage.title("Login")

    topFrame = Frame(loginPage, width=300, height=30) # formats login page
    topFrame.pack()
    bottomFrame = Frame(loginPage, width=300, height=300)
    bottomFrame.pack(side=BOTTOM)

    global pin
    global pinEntry
    pin = StringVar()

    pinLabel = Label(bottomFrame, text="Enter Pin:").pack() # gives place to enter pin
    space = Label(bottomFrame).pack()
    pinEntry = Entry(bottomFrame, textvariable = pin)
    pinEntry.pack()
    space1= Label(bottomFrame).pack()
    loginButton = Button(bottomFrame, text="Login", command=login_pin).pack()
    space2= Label(bottomFrame).pack()
    space3 = Label(bottomFrame).pack()




# REGISTER FUNCTIONS
def register_pin(): # checks inputted pin to see if its in use
    checkPin = newPin.get()
    count = 0

    fhand = open("registry.txt")
    for line in fhand:
        line = line.rstrip()
        if line == checkPin:
            count = count + 1
    fhand.close()
    if count > 0: # if yes, gives error
        error = Tk()
        error.title("ERROR")

        Label(error, width=30, height=5, text="ERROR: This pin is already in use.").pack()
    else:
        fhand = open("registry.txt", "a") # if not it adds it and prompts user to log in
        fhand.write(checkPin+"\n")
        fhand.close()

        fhand = open(checkPin+".txt", "x")
        fhand.close()

        newPinEntry.delete(0, END)

        complete = Tk()
        complete.title("Registration Complete")

        Label(complete, width=30, height=5, text="Registration complete.").pack()

        registerPage.destroy()


def register():
    global registerPage # register page
    registerPage = Toplevel(window)
    registerPage.title("Register")

    topFrame = Frame(registerPage, width=300, height=30)
    topFrame.pack()
    bottomFrame = Frame(registerPage, width=300, height=300) # formats registry page
    bottomFrame.pack(side=BOTTOM)

    global newPin
    global newPinEntry
    newPin = StringVar()

    newPinLabel = Label (bottomFrame, text="Enter a New Pin:").pack()
    space = Label(bottomFrame).pack()
    newPinEntry = Entry(bottomFrame, textvariable = newPin)
    newPinEntry.pack()
    space1= Label(bottomFrame).pack()
    registerButton = Button(bottomFrame, text="Register", command = register_pin).pack()
    space2= Label(bottomFrame).pack()
    space3 = Label(bottomFrame).pack()





# MAIN WINDOW
window = Tk()

title = Label(window, text="Contacts", bg="black", fg="white") #formats home screen
title.pack(side=TOP, fill=X)

topFrame = Frame(window, width=300, height=30)
topFrame.pack()
bottomFrame = Frame(window, width=300, height=300)
bottomFrame.pack(side=BOTTOM)

enterPin = Button(bottomFrame, text="Enter Pin",bg="white", fg="blue", command = login, width=15, height=2).pack()
space = Label(bottomFrame).pack()
makePin = Button(bottomFrame, text="Create a New Pin",bg="white", fg="blue", command = register, width=15,height=2).pack()
space1 = Label(bottomFrame).pack()




window.mainloop()
