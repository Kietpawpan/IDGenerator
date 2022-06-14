# Import the os module for opening a file in the computer
import os

# Import the tkinter module for creating graphic user interface (GUI)
import tkinter
from tkinter import *

# Import message box module
from tkinter import messagebox

# Import the webbrowser module
import webbrowser

# Import the datetime module for creating a time-based serial number
from datetime import datetime
    # Let now is the present time read from the system clock
now = datetime.now()
    # Let issueDate is the present time in this format: yyyymmddhhmmmmm
issueDate = now.strftime("%Y%m%d%H%M")
    # Convert the issueDate into the user ID number: yymmddhhmm (Delete the first two digits).
userIDNumber = issueDate[2:12]

# Create a new function called "Show Output", which gets integer number transformed from the text number input
def show_output():
    # Get the values from the two input boxes
    userName = userName_input.get()
    surName = surName_input.get()

    # Create a new dictionary for translate the username and surname into English
    # Avoid I which seems like 1 and use various English characters for Thai vowels
    myThaiDict = "กขคฆงจฉชซฌญฎฏฐฑฒณดตถทธนบปผฝพฟภมยรลวศษสหฬอฮโใไฤเแ"
    myEnglishDict = "KKKKNCCCSCYDTTTTNDTTTTNBPPFPFPMYRLWSSSHLAHZEURGV"

    # Create separate dictionary tables for username and surname translation
    myNameTable = userName.maketrans(myThaiDict, myEnglishDict)
    mySurnameTable = surName.maketrans(myThaiDict, myEnglishDict)

    # Translate the username and put the value in a new variable called transName
    transName = userName.translate(myNameTable)

    # Translate the surname and put the value in a new variable called transSurname
    transSurname = surName.translate(mySurnameTable)

    # Set the value for the output, which combines the first characters of the translated
    # username and surname plus the Integer ID
    output = '' + transName[0] + transSurname[0] + str(userIDNumber)

    # Show the output as text
    output_label.configure(
        text=output,
        # Set the output's font as Arial with the size of 25
        font=('Arial', 20)
    )

# Create a save function for recording the ID in a text file
def save_ID():
    # Create the same ID engine
    userName = userName_input.get()
    surName = surName_input.get()
    myThaiDict = "กขคฆงจฉชซฌญฎฏฐฑฒณดตถทธนบปผฝพฟภมยรลวศษสหฬอฮโใไฤเแ"
    myEnglishDict = "KKKKNCCCSCYDTTTTNDTTTTNBPPFPFPMYRLWSSSHLAHZEURGV"
    myNameTable = userName.maketrans(myThaiDict, myEnglishDict)
    mySurnameTable = surName.maketrans(myThaiDict, myEnglishDict)
    transName = userName.translate(myNameTable)
    transSurname = surName.translate(mySurnameTable)
    output = '' + transName[0] + transSurname[0] + str(userIDNumber)
    # Create a log file (.txt) that records the time and the output ID
    # First, open the file customerID.text for appending (To add new info, not overwrite).
    # Allow Thai text to write in the text file (utf-8)
    customerIDFile = open("customerID.txt","a", encoding="utf-8")
    # Create a timestampt
    timeStampt = str(datetime.now())
    # Write timestampt in the new line
    customerIDFile.write(timeStampt + "\n")
    # Indend in the next line
    customerIDFile.write(" ")
    # Write the customer name and surname in Thai
    customerIDFile.write(userName + " ")
    # Write the output (or customer ID) in the new line
    customerIDFile.write(output + "\n")
    # Close the file
    customerIDFile.close()
    # Show the message box to notify the user the Save ID is done.
    messagebox.showinfo("Save ID","Done!")

# Create a Check ID function. To open the customer ID file
def checkID():
    # Define which file is the customer ID file
    customerIDFile = "CustomerID.txt"
    # Use the default editor to open the file
    os.startfile(customerIDFile)

# Create Open Readme function. To open the url
def openReadMe():
    # Define which url to pen
    webbrowser.open('https://github.com/Kietpawpan/IDGenerator#readme')

# Create a graphic user interface (GUI) for this application
window = Tk()

# Set the size of the GUI as 450 x 200 px
window.geometry("500x300")

# Set the name of my app as Lotto 2022.
window.title("jTech")

# Set the text on what this app does and show it in the window with space between lines at 20 px.
title_label = tkinter.Label(master=window, text='ID Generator')
title_label.place(x=220, y=10)

# Create two text messages to describe the two input boxes, with font size = 12
userName_text = Label(text="ชื่อผู้ยื่นคำขอ", font=("", 10))
surName_text = Label(text="นามสกุล", font=("",10))

# Set the locations of the text
userName_text.place(x=15,y=40)
surName_text.place(x=15,y=120)

# Set the type of input data as String (plain text)
firstName = StringVar()
lastName = StringVar()

# Create an input box for the first name of the user, and set its location
userName_input = tkinter.Entry(textvariable=firstName, width=20, font=("",12))
userName_input.place(x=15,y=20)

# Create an input box for the surname, and set its location
surName_input = tkinter.Entry(textvariable=lastName, width=20, font=("",12))
surName_input.place(x=15,y=100)

# Add a button, named 'Get ID', and add this command: 'show_output'.
# Set the button size as
getID_button = tkinter.Button(text='Get ID',
    command=show_output, width=15, height=2
)
# Place the button on the screen
getID_button.place(x=220,y=50)

# Add another button for saving the ID
save_button = tkinter.Button(master=window, text='Save ID',
    command=save_ID, width=15, height=2
)
# Place the button on the screen
save_button.place(x=220,y=100)

# Add a check ID button
check_button = tkinter.Button(master=window, text='Check ID',
    command=checkID, width=15, height=2
)
# Place the button on the screen
check_button.place(x=220,y=150)

# Add Readme button
readme_button = tkinter.Button(master=window, text='Read Me',
    command=openReadMe, width=15, height=2
)
# Place the button on the screen
readme_button.place(x=220,y=200)

# Show the output on the screen with 20 px space vertically
output_label = tkinter.Label(master=window)
output_label.place(x=220,y=250)

# Show the app window
window.mainloop()

# Design a message box to show after the user click the Save ID button
saveInfoBox = Tk()
saveInfoBox.geometry("300x200")
saveInfoBox.mainloop()

# Prevent the console window from opening, by saving this file as IDGen.pyw instead of .py
# Store this file on Desktop or any folder for ease.
# This program is developed by Monte & Jeerawish Kietpawpan