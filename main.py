'''
# Empty contact book creation....
contact_book = {}
while True:
    # asking for user choices....
    choice = input("Please enter the choice (S/F/D/E)\nS==> Save the contact\nF==> Find contact\nD==> Display contact\n"
                   "E==> Exit\n").upper()
    # working of choice save....
    if choice == "S":
        name = input("Enter person name:-\n")
        contact = input("Enter phone number\n")
        contact_book[name] = contact
        print("-------------------------------------")
        print("Phone no. is saved successfully !")
        print("-------------------------------------")
    # working of choice find contact...
    elif choice == "F":
        find_person = input("Enter name of person to find contact:-\n")
        print("-------------------------------------")
        print("The number of ", find_person , " = ", contact_book[find_person])
        print("-------------------------------------")
    # working of choice show all contact...
    elif choice == "D":
        print("-------------------------------------")
        print(contact_book)
        print("-------------------------------------")
    elif choice == "E":
        break

'''
# import the tkinter module...
from tkinter import *
# import the os module to perform os functions...
import os
# initialization of tkinter module as name "root" of main window...
root = Tk()
# setting width x height of root window...
root.geometry("300x500+520+30")
# naming te title to the window to display the user...
root.title("Phone Book Project")

# empty dictionary creation ...
contact_book = {}

# save function ...
def save():
    # get field one value as string
    person_name = nameBox.get()
    # get field second value as string
    phone_number = numberBox.get()
    # putting name as key and phone number as value
    contact_book[person_name] = phone_number


# find function ...
def find():
    person_name = nameBox.get()
    # lb to show the phone number to be searched
    lb = Label(root, text=contact_book[person_name], font=16)
    lb.pack()


# showAll function ...
def showAll():
    # root2 for display output on other windows tab
    root2 = Tk()
    root2.geometry("300x500+550+40")
    # check for empty phone book
    if contact_book == {}:
        lb = Label(root2, text="Empty phone book")
        lb.pack()
    # if not then save the number
    else:
        # k for keys and v for values
        for k, v in contact_book.items():
            lb = Label(root2,text=f"{k} = {v}")
            lb.pack()
    root2.mainloop()


# close function ...
def close():
    exit(os)

# variable of entry boxes...
nameBox = StringVar()
numberBox = StringVar()

# labels .....
name_label = Label(root, text="Enter person name...   ", font=14)
name_label.place(x=50, y=100)
number_label = Label(root, text="Enter phone number...", font=14)
number_label.place(x=50, y=200)

# entry boxes...
name_entry = Entry(root, width=30, relief=RIDGE, bd=5, textvariable=nameBox)
name_entry.place(x=50, y=120)
number_entry = Entry(root, width=30, relief=RIDGE, bd=5, textvariable=numberBox)
number_entry.place(x=50, y=220)

# buttons ...
save_btn = Button(root, text="save", width=10, height=1, font=14, command=save, bg="LightGreen")
save_btn.place(x=50, y=300)
find_btn = Button(root, text = "find", width = 10, height = 1, font = 14, command=find, bg="Yellow")
find_btn.place(x=150, y=300)
showAll_btn = Button(root, text="show all", width=10, height=1, font=14, command=showAll, bg="LightBlue")
showAll_btn.place(x=50, y=350)
close_btn = Button(root, text="close", width=10, height=1, font=14, command=close, bg="IndianRed1")
close_btn.place(x=150, y=350)

# binding the window in a loop so that it captured the output window...
root.mainloop()