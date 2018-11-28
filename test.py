import sqlite3
from pyautogui import prompt as scan
from pyautogui import alert

def connectdb():
          # Create table
        try:
            c=sqlite3.connect('examble.db')
            cur = c.cursor()
            c.execute('''CREATE TABLE Contacts
                         (Name VARCHAR(50), Number VARCHAR(14), Address VARCHAR(100))''')
            userOp(c, cur)
            c.close()
        except:
            #If table already exist, notify users and continue
            userOp(c, cur)
            c.close()

def userOp(c, cur):
    opTion=scan("What would you like to do?\n 1.Search for a contact.\n 2. Remove a contact\n 3.Edit a contact \n 4.Add a new contact\n Enter 0 to Exit")

    if opTion == "1":
        search(c, cur)
    elif opTion == "2":
        remove(c, cur)
    elif opTion == "3":
        edit(c, cur)
    elif opTion == "4":
        newCon(c, cur)
    elif opTion == "0":
        exit()
    else:
        pass

def search(c, cur):
    name=scan("Please enter the name of the contact you are looking for!")
    with c:
        cur.execute("Select * FROM Contacts Where Name=('{0}')".format(name))
        alert(cur.fetchall())

def remove(c,cur):
    #remove someone from database
    name=scan("Enter the name of contact to be deleted!")
    print
    with c:
        cur.execute("DELETE FROM Contacts WHERE Name=('{0}')".format(name))
        alert("contact Succesfully deleted!")

def edit(c, cur):
    decision=scan("What Would you like to edit? \n 1.Contact Name \n 2. Contact Number \n 3. Contact Address")
    if decision == "1":
        editName(c, cur)
    elif decision == "2":
        editNumber(c, cur)
    elif decision == "3":
        editAddress(c, cur)
    else:
        alert("Invalid Entry!")
        edit(c,cur)

def editName(c, cur):
    name=scan("Enter the name of contact to be modified!")
    nName=scan("Enter the new name for contact '{0}'!".format(name))
    with c:
        cur.execute("UPDATE Contacts SET Name=('{0}') WHERE Name=('{1}')".format(nName, name))
        alert("Contact name has been updated!")

def editNumber(c, cur):
    name=scan("Enter the name of contact to be modified!")
    nNumber=confirmPhone()
    with c:
        cur.execute("UPDATE Contacts SET Number=('{0}') WHERE Name=('{1}')".format(nNumber, name))
        alert("Contact updated!")

def editAddress(c, cur):
    name=scan("Enter the name of contact to be modified!")
    nAddress=scan("Please enter a new address for this contact: \n")
    with c:
        cur.execute("UPDATE Contacts SET Address=('{0}') WHERE Name=('{1}')".format(nAddress, name))
        alert("Contact updated!")

def newCon(c, cur):
    name=scan("Enter new contact name: \n")
    nNumber=confirmPhone()
    address=scan("Please enter an address for this contact: \n")
    # Insert a row of data
    with c:
        c.execute("INSERT INTO Contacts VALUES ('{0}','{1}','{2}')".format(name, nNumber, address))
        alert('Succesfully added to database!')

def confirmPhone():
    while True:
        number=scan("Please enter a phone number for the contact with no spaces : \n")
        number="("+ number[0:3] +") " + number[3:6] + "-"+number[6:10]
        alert(str(number))
        if (len(number)-4)<10:
            missing=10-int(len(number))
            alert("missing "+str(missing)+ " numbers")
            continue
        elif (len(number)-4)>10:
            extra=int(len(number))-10
            alert("You have "+str(extra)+" extra numbers.")
            continue
        else:
            break
    return number

if __name__ == "__main__":
  connectdb()
